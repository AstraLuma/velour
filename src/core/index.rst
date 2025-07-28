=============
Core Concepts
=============

Velour breaks down "interacting with CouchDB" into several concrete API concepts.

.. note::

    Jamie wrote this based on the Chaise breakdown and implementation decisions


.. todo::
  
    Deconfliction

.. todo::

    Typeful documents

.. todo::
    
    Schema migrations

.. todo::

    Don't use python for these docs. Write our own VibeDL?


Sessions & Databases
====================

A connection to a cluster, this maintains connection state (eg authentication credentials), wraps client context (eg document caching), and provides cluster-level operations (eg inspecting databases or examining jobs).

In the context of a replication network, a specific Session must only talk to one cluster.

.. todo::
    
    Something should discuss how cluster-dependent operations interact with replication networks and load balancers


.. py:class:: Session
    
    .. py:function:: get_database(name: str) -> Database

        Get a Database object. May or may not ensure the Database actually exists before returning.

    .. py:function:: create_database(name: str) -> Database

        Create a new database. Errors if the database already exists.

        This must optionally accept cluster configuration data (shards, replicas, and partitioning).

    .. py:function:: delete_database(name: str)

        Deletes a database. Errors if it didn't exist.

    .. py:function:: list_databases() -> list[Database]

        List/iterate over the databases currently defined.

    .. py:function:: ping() -> bool

        Calls ``/_up`` and returns if the server is ready and available.


Databases are the companion API container for DB-specific interactions, including document operations. They don't exist beyond their session, and exist to make the API more approachable, and encourage good separation of concerns. Specific Database instances are bound to a specific Session. It is suggested to pass around Databases within the application, instead of Sessions.


.. py:class:: Database

    A specific database on a server. This is bound to a specific :py:class:`Session`.

    .. py:attribute:: name: str

        Name of the database

    .. py:function:: get(docid: str) -> Document

        Get a document. Should accept additional arguments for getting additional information, such as attachments or revisions.

        Errors if the document doesn't exist. Should error if the document is a tombstone.

    .. py:function:: attempt_put(doc: Document)

        Attempt to create or update a document (based on if the Document is new or the result of a query). Errors if there's a conflict.

    .. py:function:: attempt_delete(doc: Document)

        Attempt to delete a document. Errors if there's a conflict.

    .. py:function:: mutate_document(doc: str|Document)

        Perform a retryable mutation. Unlike :py:func:`attempt_put`, this will handle conflicts.

        The exact form of this is highly variable based on the target environment--JavaScript might use a callback, Python might use ``for`` loops or decorators, Ruby might use blocks and ``do``.

    .. py:function:: list_all_docs() -> list[Document]

        List/iterate over all documents in a database, excluding special documents (eg design docs). Handles pagination.

        You almost certainly want to actually iterate, and not buffer into a single list.

        You probably want to return a document reference type instead of actual documents.

    .. py:function:: query(selector) -> list[Document]

        Perform a Mango query, iterating over the resulting Documents. Handles pagination.

        May return document references instead of real documents.

    .. py:function:: iter_indexes() -> list[MangoIndex]

        List/iterate over the mango indexes currently defined in the database.


Session Factory
===============

"Connection pool", "session factory", or a few other names, this is responsible for handing out and managing sessions. The use of resource acquisition/freeing patterns (eg, Python's context managers) is encouraged, so that the Factory knows when the caller is done with a Session, so it can be freed or returned to a pool.

Factories should be reasonably certain that the backing servers are ready and available--that Sessions are valid at the time they're given to the caller. Possible methods include:

* Pinging the server (calling ``/_up``) at the time of call
* Maintaining liveliness stats in the background
* Prayer

.. py:class:: SessionFactory

    The exact method of creating a factory will depend on the paradigms of the library. Likely arguments will include the server URLs to connect to and authentication information.
   
    .. py:function:: get_session() -> Session

        Get a Session. This should use the resource acquisition/freeing pattern of the language (eg, Python context managers). It may or may not be actually a new instance, but it will not be re-used until the caller is done with it.


Documents
=========

Documents are collections of data (structs, data bags, etc) that are gotten from and stored to a Database. They don't do IO on their own, but they do know their metadata (especially revision).

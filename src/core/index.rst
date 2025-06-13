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

    Specific lists of operations


Sessions & Databases
====================

A connection to a cluster, this maintains connection state (eg authentication credentials), wraps client context (eg document caching), and provides cluster-level operations (eg inspecting databases or examining jobs).

.. todo::
    
    Something should discuss how cluster-dependent operations interact with replication networks and load balancers


Databases are the companion API container for DB-specific interactions, including document operations. They don't exist beyond their session, and exist to make the API more approachable, and encourage good separation of concerns.


Session Factory
===============

"Connection pool", "session factory", or a few other names, this is responsible for handing out and managing sessions.


Documents
=========

Documents are collections of data (structs, data bags, etc) that are gotten from and stored to a Database. They don't do IO on their own, but they do know their metadata (especially revision).

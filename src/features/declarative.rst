============================
Declarative Design Documents
============================

It is useful for an application to describe design documents in a declarative way, similar to how an ORM might have a schema definition for a SQL database. Velour clients may implement a method of applying this declaration to a live database.

.. note::
    
    This is just documenting how chaise does it. This doesn't really align with CouchDB best practices.

Declarations
============

These declarations are defined via a series of `KDL`_ files in a directory. Each database is a directory with a ``__db__.kdl`` file, with some number of additional ``.kdl`` files defining design documents.

.. _KDL: https://kdl.dev/

Databases
---------

The database file ``__db__.kdl`` indicates a directory is defining a CouchDB database.

The ``__db__.kdl`` file may be empty:

.. code-block:: kdl
   :caption: __db__.kdl

Or it can have a empty ``database`` node:

.. code-block:: kdl
   :caption: __db__.kdl

   database

Or it the database name can be changed:

.. code-block:: kdl
   :caption: __db__.kdl

   database "foo/bar"

.. TODO::
    
    Sharding parameters

Design Documents
----------------

Each design document is defined by a single ``.kdl`` file next to the ``__db__.kdl`` file. It may be empty, define one or more indexes (for use with mango), or define one or more views. Note that due to limitations in CouchDB, you cannot define indexes and views in the same design document.

Indexes
~~~~~~~

Each index consists of a name and one or more fields. They can be listed individually:

.. code-block:: kdl
    :caption: long-kdl.kdl

    index "foo" {
        field "spam"
        field "eggs"
    }


Or together:

.. code-block:: kdl
    :caption: short-kdl.kdl

    index "bar" {
        fields "quux" "baz"
    }

(These styles can be mixed and matched.)

.. TODO::

    json vs text, partial

Operations
==========

There's one major operation in this: apply. Indexes aren't evolved, just rebuild, so there is no migrate forward or migrate back.

apply
-----

Given a server and a directory declarations, create databases and apply declarations.

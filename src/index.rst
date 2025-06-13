======
Velour
======

Velour is a language- and environment-agnostic "specification" for rich CouchDB clients.

By "rich", we mean clients that are more than just API wrappers. Clients that provide utilities to more robustly mutate documents, provide ORM-like declarative de/serialization, handle revision conflicts, and other concerns important for mature use of CouchDB.

By "specification", we mean a set of shared concepts and some specific protocols. Conforming clients won't match exactly, but they should rhyme. This makes Velour a lot more vibes-based than most technical specifications.


.. toctree::
    :caption: Contents
    :titlesonly:

    intro
    core/index
    features/index
    specs/index


Goals
=====

The hope is that Velour-conforming clients will exhibit some themes:

* Clients that share concepts: they'll use similar ideas expressed in a way that best work for their language and environment
* Clients that provide usable abstractions over common API calls: things like mutation loops, pagination, changes following, etc
* Clients that provide structure for opinions and intrinsic complexity: converting between JSON and an application model, typeful documents, conflict resolution, schema migration, and other usage-specific concerns
* Client compatibility: Doing all of the above, while allowing the browser to use a JavaScript client and the server to use a Python client and they won't fight.


Non-goals
=========

Velour clients are not:

* Storage engines: This is not a direct sister project to PouchDB/CouchDB, but an additional layer on top


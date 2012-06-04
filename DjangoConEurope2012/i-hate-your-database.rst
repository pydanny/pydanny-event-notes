====================
I hate your database
====================

by Andrew Godwin

    * Lead developer for South http://south.aeracode.org/
    * Cheese fan
    * http://twitter.com/andrewgodwin
    
Hate? Databases?
==================

Countering

* Misuse
* Ignorance
* Lies

Different Databases, different occasions
==========================================

* People use the same database for everything they touch
* You shouldn't use a database for things it was not designed to do.
* Types of databases:

    * Relational
    * Document
    * Key-value
    * Graph
    * Object / Heirarchial
    * Spatial
    * Time-series / RRD
    * Search

* Relational

    * PostgreSQL
    * MySQL
    * SQLite

* Document

    * MongoDB
    * CouchDB
    
* Key-value

    * Redis
    * Riak
    
Some quick theory
==================

* ACID

    * Atomicity
    * Consistency
    * Isolation
    * Durability
    
* CAP Theorem (you can only have 2 of the 3 of them)

    * Consistency
    * Availability
    * Partition Tolerance
    
MySQL
=====

Very interesting database system

* No transactional DDL
* Poor query optimizer
* MyISAM: full-table locking, no transactions
* Oracle
* Very fast for some operations

SQLite
========

* Little integrity checking
* Impossible to do some table alterations
* No concurrent access
* Low overhead
* Very portable

PostgreSQL
===========

* Slow default configuration
* Can be a little harder to learn
* Almost too many features
* Incredibly reliable

MongoDB
=======

* No fixed schema
* Very similar to Python types
* Immature (but improving)
* No transactons
* No integrity checking

Key/value stores
==================

Redis, Riak, memcached

* Horizontal scaling (but with drawbacks)
* Extremely fast
* Can only fetch objects by key
* Batch/map-reduce queries
* Transactions not possible

Spatial databases
==================

* Knowledge of projections useful
* Spatial indexes really speed up some problems
* Generally add-on to existing DB
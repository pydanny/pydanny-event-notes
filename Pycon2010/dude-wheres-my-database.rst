Dude, where's my database?
==========================

by Eric Florenzano

Relational
=============

 * Highly structured
 * Strong type system
 * Powerful query language
 * Python talks to all of them
 * In common use

Problems
---------

 - Hard to scale

----

Key/Value
=========

 * Tracking HTTP sessions
 * User references
 * URL shorteners
 * simple and fast
 * Examples:

  * gdbm
  * Kyoto Cabinet
  * Berkely DB
  * MemcacheDB

Problems
----------

 - No interesting queries
 
---- 
 
Data Structure
===============

 * Super fast
 * Maps to certain problems very well.
 * Modification of key/value
 * Structured values
 * Atomic operations
 * Example:
 
  * Redis
  
Problems
----------

 - Lack of alternative implementations
 
----- 
 
Graph
=======

 * Store data as nodes and edges in a graph
 * Fits logically to many problem spaces
 * Programmatic queries
 * Examples:
 
  * Neo4j
  * VertexDB
  
Problems
-----------

 - Scale ceilings
 - Lack of alternative implementations
 
Document-Oriented Database
===========================

 * Unstructured
 * Formatted (JSON, Python object)
 * Programmable Query API
 * Examples:
 
  * CouchDB
  * MongoDB
  * ZODB
  
 * Use Cases:
 
  * Activity streams
  * User data
  * CMS
  
Problems
---------

 - Scale ceiling
 - Implementation-specific weaknesses
 
----
 
Highly Distributed Databases
=============================

 * Optimized for multi-node
 * Add and remove nodes on the fly
 * Hard to do ad-hoc queries
 * Sacrifice consistency
 * Examples:

  * Cassandra
  * Riak
  * HBase
  * Hypertable
  
Problems
---------

 - Eventual consistency
 - Can't do efficient ad-hoc queries 
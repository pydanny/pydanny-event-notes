=====================
History of SQLAlchemy
=====================

 * 0.1 - 2006, very small API, threadlocal, ActiveMapper added to handle objects nicely
 * 0.2 - Lots of users, changed the API to be closer to today, inspired by Hibernate, Threadlocal turned off, wrote very fast
 * 0.3 - Rewrite a lot internals, ORMs reorganized, users needs evaluated, API stabilized
 * 0.4 - Here come developers to help out!, Lots of internal refactoring, speed profiling done, SQL expressions constructs done, lots of transactions and support for more databases.
 
Highlights of 0.4
-----------------
 * Much faster than 0.3
 * Underlying code is simplified
 * lots less callcounts and redundant method calls
 * Smart operators in SQL calls to handle different database types

SQL Expression language
-----------------------
 * s - select([employees,c.id, employees,c.name])
 * select([func.now()]) will work with SQLlite!
 
New ORM Query ORM
-----------------
 * Query object is fully generative.  Mapped properties now have relational operators
 
Inline Aliasing
---------------
 * Alternate table ids to handle self-referencing tables in order to map out heirarchical data
 * All the work can be filtered against a single query expression
 * Easy dialogue making it very easy to implement
 * In 0.4, join() generates aliased joins and aliases criterion for you
 
High level operators
--------------------
 * Has and Any are synonyms for SQL exists() method.

New ORM Configurations
----------------------
 * In SQL 0.4.4 familiar table and mapper constructs can be moved into class declarations called 'New Declarative Layer'.  


Collections API
---------------
 * Sets, dictionaries, and any user-defined collection may be mapped using an open API
 * This means any python collection object can be used by SQLAlchemy
 * Use declarations to turn any object of your choice into SQLAlchemy objects.  NICE!

Dynamic Relations
-----------------
 * Very large collections can be managed by a 'dynamic' relation, which issues queries for every access
 * This way you don't have to load a gigantic item into memory, just intelligent bits.  A few restrictions, but it speeds things up
 
Polymorphic Inheritence
------------------------
 * Whole inheritence hierachies can be loaded automatically
 * So mapping out standard fields in a table (Title, Description, Create, etc) is easy.  This was a gotcha in that Django effort, remember?
 * Can use to specify criteria against a subclass.

New transactional features
--------------------------
 * Session can be configured to be 'always transactional', and optionally auto-flushing
 * Databases which supprt SAVEPOINT can nest transactions
 * Connections and ORM sessions both support two-phase commit semantics for supported databases
 
Other features
--------------
 * ORM supports mutable primary keys, ON UPDATE cascade.
 * Arbitrary SQL expressions can be asssigned to object attributes for 'atomic' update behavior
 * metadata.reflect() can load full schemas at once
 * New dialacts: MaxDB, Sybase, Access, Informix, DB2
 * Horizontal sharding: extension for ORM, transparently loads and saves rows across multiple databases

What is coming back
-------------------
    * Migrate is back!
    * Dialects will soon decouple SQL compilers from DBAPI behavors, allowing reuse among JDBC, ODBC, multiple native DBAPI connectors
    * Jython support
    * Customize class instrumentation; PJE using it to integrate with Trellis
    * SQLAlchemy books
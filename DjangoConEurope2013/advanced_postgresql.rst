====================================
Advanced PostgreSQL in Django
====================================

* by Christophe Pettus

PostgreSQL is the most advanced open-source database on the planet, but (except for GeoDjango) few Django developers take advantage of its more advanced features. We want to change that!

We'll talk about custom types (including Admin integration), replication tricks, specialized indexes, unstructured types such as JSON, stored procedures, and other ways to get maximum functionality and performance out of your PostgreSQL data store.

Database Agnosticism
======================

* Django has to be able to handle all databases.
* That means it loses special features of individual database systems (PGSQL, MySQL, etc).
* Database migration is a once in a lifetime thing.


What can PostgreSQL do for you
================================

* PostgreSQL has a huge range of built-in types
* Most can be used natively in Django
* You can find libraries to support them.

citext
--------

    * case insensitive text
    * ignores case on comparisons for a field
    
hstore
-------

    * built-in dict-like structure
    * Maps to Python dict
    * Can be indexed and queried for inclusion
    * requires custom sql
    
json
------

    * All the cool kids use NoSQL databases
    * Something faster than MongoDB to store your JSON databases
    * validated going in
    * Not feature rich, but it's growing
    
Others
-------

* UUID
* IPv4 and IPv6
* Interval - stores time intervals directly in the database
* See Craig's talk later
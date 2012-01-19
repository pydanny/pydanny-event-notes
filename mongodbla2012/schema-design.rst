==========================================
Schema Design
==========================================

by Kevin Hanson, Solutions Architect, 10gen

Parallels
==========

Tables == Collections
Row == Document
Column == Field
Index == Index
Join == Embedding & Linking
Schema Object == None

The Big Question
=================

Do we link or do we embed?

Blog posts and comments

Embedded
---------

* Faster
* But large embeds can make the master document slow. Ex: If a post has a billion comments

Linked
--------

* Slower
* Returning the master document requires extra logic

Each comment gets own doc
--------------------------

Comment gets its own copy of the master blog post

* Fast but inverted
* Great if you have gajillions of comments
* Even more logic

Denormalization
=================

* Caching via memchached, redis, etc are functionally denormalized instances of data sets.
* NoSQL means you cut out the middleman

More thoughts on denormalized data

* Faster than normalized
* More object-oriented
* application level applications

Managing Arrays
=================

* Pussing to an array infinitely

    * Document will grow larger than Pre-allocated size
    * Document may increase max doc size of 16MB
    
Sometimes you have to limit size of an array
---------------------------------------------

Logic idea::

    first 200 comments are insert into the blog document
    After that have a linked comment document
    
Schema decisions when sharding
===============================

* Can we intelligently partition data?
* Will this partitioning create hotspots?
* Can our partitioning actually improve overall performance?

Bad shard key::
    
    Sharding on "date" field and constantly inserting most recent data...
    
Good example::

    sharding blog posts on "author"
    
.. note:: TODO find out why the Good example is actually good
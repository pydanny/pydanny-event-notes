==========================================
Indexing & Query Optimization
==========================================

by Kevin Hanson, Solutions Architect, 10gen

High level
==========

* What's an index and why do we need one?
* As we insert data into MongoDB, we store that as a linked list
* So if you search for something in 7 documents, it has to search in all 7 of them


Creating indexes in MongoDB
===================================

 * You can index anything
 * All docs have an `_id` field that is auto-indexed
 * new indexes:
 
.. sourcecode:: javascript 

    db.blog.save({author: "James", ts: new Date()}) 
    db.blogs.ensureIndex({Author: 1, ts:-1})

Things to know about indexes
================================

* Slows down writes
* But speeds up reads!
* Forces uniqueness on a title

.. note:: TODO - check that we don't have dupe titles

Covered Index
===============

* Query resolved in index only
* Eliminated need to pull documents from DB
* NEed to exclude `_id` from items projected.

.. sourcecode:: javascript 

    db.blogs.save({
        author:"Kevin",
        editor:"Katie"
    
    })
    db.blogs.ensureIndex({author: 1, editor: 1});
    db.blogs.find({author}) // TODO finish this
    
Spare Index
=============

* Key value included if and only if the value is present
* Reduces the size of index
* Limited to a single field

.. sourcecode:: javascript 

    // TODO fill this out
    
Unique Sparse Index
===================

* Key value included if and only if the value is present
* Reduces the size of index
* Limited to a single field
* Null and not-present are different

.. sourcecode:: javascript 

    // TODO fill this out
    
Geospation indexes
===================

* Geo hash stored in B-Tree
* First two values indexed

Query Performance Analysis 
===========================

.. note:: Speaker had to go super fast here because he kept answering questions. This is why you ask people to wait for the Q&A at the end.


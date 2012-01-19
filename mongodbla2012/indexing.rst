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
 * All docs have an _id field that is auto-indexed
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


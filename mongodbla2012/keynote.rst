================================================
Keynote: Welcome and What's new in Mongo DB
================================================

by Paul Pederson, Deputy CTO, 10gen

Design Goal: Rich data model
-----------------------------------

* JSON/BSON documents
* Good mapping to native programming language types
* Flexibility for dynamic data
* Better data locality
* Schema-free or dynamic schema

Footnote to design goal
~~~~~~~~~~~~~~~~~~~~~~~

(DB degrees of freedom)

* Zero degrees of freedom: static queries, static data 
* One degree of freedom: dynamic queries, static schema (Relational DB)
* Two degrees of freedom: dynamic queries, dynamic schema (NoSQL DB)

General-purpose DBMS
=====================

* Sophisticated secondary indexes
* Dynamic queries
* Sorting
* Rich updates, upserts
* Easy aggregation
* Viable primary data store

Design Goal: Web Scale
======================

* Scale linearly with *sharing*
* Say 'no' to distributed joins
* Increase capacity with no downtime
* Make scaling transparent to the application

Design Goal: Minimal knobs
===========================

* Make it easy to deploy and manage
* Find natural default configuration options
* Do the right thing out of the box

Release History
================

* 1.0 August 2009: supported bson and BTree range query optimization
* 1.2 December 2009: map-reduce
* 1.4 March 2010: Background indexing, geo indexes
* 1.6 August 2010: sharding, replica sets
* 1.8 March 2011: journaling, sparse, and covered indexes
* 1.10 = 2.0: September 2011: cumulative changes

Changes in 2.0
===============

Here we go...

Journaling improvements
-------------------------

* Enabled by default for 64-bit platforms
* Journal is compressed for faster commits to disk
* `--journalCommitInterval` command line option exists for specifying some neat feature
* May wait for group commit on write with `j=true` arg to `getLastError()`

Compaction improvements
------------------------

.. note:: run this after adding an index

* Collection-level command::

    db.mycollection.runCommand('compact');
    
* Copies extent-by-extent using a single 2GB scratch space
* BUilds all the indexes at the end in parallel:

    * First half off external sort occurs while copying extent data. For each doc find all index keys and store these and process.
    
Index improvements
------------------------

.. note:: Once you migrate to 2.0 the index changes are not reversable

* Keeping the index working set in RAM is important
* v.20 indexes are 25% smaller than v1.8 indexes
* Index compression arises by optimization of BTree index key BSON representation

Concurrency improvements
--------------------------

* Yielding mitigates reader-witer lock contention
* In general mongodb yields all the time long table scan, yield every 100
* IN v2.0 we now yield around page faults.

Map-reduce performance
----------------------

* About 3x faster in 2.0 over 1.8


THings to follow up on:
---------------------------------

.. note:: TODO find out what was given in terms of improvements

* Priorities
* Replica set force reconfigure
* Durability

New features
----------------

* Multiple location geo search
* Map-reduce sharded output
* Query syntax: $and
* Custom shell prompts

Links
------

* http//v.gd/mongodb20
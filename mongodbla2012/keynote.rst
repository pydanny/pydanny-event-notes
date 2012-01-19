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
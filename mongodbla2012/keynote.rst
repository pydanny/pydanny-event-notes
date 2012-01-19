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
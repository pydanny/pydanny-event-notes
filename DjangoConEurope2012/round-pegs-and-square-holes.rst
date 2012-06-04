=======================================================
Round pegs for square holes - using mongoDB with Django
=======================================================


* Audrey Roy and Daniel Greefeld
* Cartweel people
* Using mongoDB with Django
* Taken by @chrisglass

.. note:: Hard to keep up here

MongoDB
=======

* Mongo is NoSQL, stores stuff in BSON, uses javascript (V8), bindings for pretty much
  anything available.
* Collections are like tables, Documents are like rows.
* Queries return a list of dictionnaries.

Many options
============

pymongo
-------

* Plenty of connectors available, pymongo being the "official" one, that most others wrap.
* Schemaless, very fast, supported directly by 10Gen.
* You loose modelforms, some admin

MongoEngine
-----------

* Mongoengine is another option. It is a more Django looking piece of code, Integrates
  better with all the django bells and whistles. VERY FAST development (basically Another
  import instead of django.model)
  A con is that it's very close to the normal way of having schemas, which is counter
  intuituve in a schemaless DB, and you loose the django admin layer.

MongoKit
--------
* MongoKit: Makes queries a little less Djangonic, more like MongoDB, therefore
  easier to go "schemaless". A litte slower, but admitedly no benchmarks <not sure it matters anyway compared to the DB-server roundtrip>

Django-nonrel
-------------
* Django-nonrel with a mongodb backend: "a patch to django", it's actually a fork
  of django. You can use django as you would normally, still lagging behind The
  rest of django, multi-db is confusing

Conclusions and further thoughts
================================

* Django doesn't really feels like a good match for NoSQL, and better suited for relational DBs
* Mongo is a greate DB, but the is some work to be done to simplify usage of Mongo, "lack of ai simple bridge".
* If you have a schema definition anyway (models), why should you not use postgres and reap all the good stuff people wrote?
* Treat instrospection like MongoDb queries? To investigate
* Schemaless databases bring great advantages on the other hand - it is should be worth a few compromises.

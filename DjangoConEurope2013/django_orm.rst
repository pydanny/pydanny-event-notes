======================================================
Getting past the Django ORM limitations with Postgres
======================================================

by Craig Kersteins

    * Heroku guy
    * http://craigkerstiens.com
    * https://twitter.com/craigkerstiens
    

With most frameworks the ORM attempts to treat all databases equally, this results in developers being limited in how many advantages they can take of their database. In particular Postgres has many features which developers would love to take advantage of but are not easily accessible via the Django ORM.

.. note:: I'm going to mention the  https://www.djangopackages.com/grids/g/postgresql-integration/ grid.

Public Service Announcements
==============================

* Postgres.app

Why PostgreSQL?
================

* It's the emacs of databases

    * Platform to build things on
    * Many built-in extensions
    
* Datatypes
* Conditional index

Limitations with Django
========================

* The ORM works with too many different databases
* Lowest common denominator

    * Django ORM has few datatypes
    * Indexes are limited compared to pure PostgreSQL
    
But Django isn't too bad

What PostgreSQL does that's cool
==================================

Datatypes:

* Arrays datatype
* hstore

    * does what MongoDB does but inside of PostgreSQL!
    * Stores in JSON
    * Getting better in PostgreSQL 9.4

Queueing
---------

Normally doing this in a database is a bad idea. So we use Redis and other resources. PostgreSQL has pub/sub and makes a great queue. You can get it working via celery with::

    pip install celery trunk
    
Text Search
------------

Instead of Lucene, Sphinx, or Solr you can use PostgreSQL for full text search. 

.. note:: Is there a Django extension?

Indexes
-------

You should generally use a BTREE index. Depending on your use case, you may need other indexes.

Flip to Read Only Mode
-----------------------

If you need to do system changes, you can make your site output only by turning on PostgreSQL's read-only mode. How cool is that?

Connections for Django
------------------------

* Django right now doesn't have persistent DB connections (not until Django 1.6 anyway)
* It has to reconnect all the time to the database, which is a performance hit.


PostgreSQL resources
=====================

* My favorite is this `PostgreSQL book`_.

.. _`PostgreSQL book`: http://www.2scoops.co/high-perf-postgresql/


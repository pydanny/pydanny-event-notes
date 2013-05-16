======================================================
Getting past the Django ORM limitations with Postgres
======================================================

by Craig Kersteins

    * Heroku guy
    

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



PostgreSQL resources
=====================

* My favorite is this`PostgreSQL book`_.

.. _`PostgreSQL book`:: http://www.2scoops.co/high-perf-postgresql/
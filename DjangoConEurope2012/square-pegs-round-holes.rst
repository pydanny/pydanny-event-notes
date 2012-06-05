========================================================
Square pegs and round holes - Django and MongoDB
========================================================

BY DANIEL GREENFELD AND AUDREY ROY
-----------------------------------

.. note:: Obviously not taken by Daniel as he's talking. This version by Marc
    Tamlyn (`@mjtamlyn<http://twitter.com/mjtamlyn>`_).

* Danny might cartwheel...
* Work at cartwheel web - a django consulting shop. Met at Pycon 2010. Engaged!

What is MongoDB?
----------------

* NoSQL
* Fast, indexable...
* Schema-less
* C++, Uses BSON (extended JSON), JS internals, Bindings in EVERYTHING. There's
  a big community.

Analogies
---------

* Collections ~ Table
* Document ~ Row
* A QS looks like a list of dictionaries.

.. code-block::

    collection = []
    document = {
        '_object_id': ObjectId('sadfasdfasdfsa'),
        'name': 'PyDanny'
    }
    collection = [document,]

Connectors
----------

* pymongo (low level)
* mongoengine/mongokit (Document ORM)
* Django non-rel

PyMongo
-------

* Official binding.
* powers everything else
* low level, but nice enough api.

.. code-block::

    connection = pymongo.Connection()
    db = connection.db
    
    for review in db.reviews.find({'rating': 3}):
         review['title']

* FAST!
* Schema crazy! (each row has its own schema)
* Supported directly by 10gen who make Mongo. Their recommended solution.

Cons
''''

* Very low level.
* Lose all of the things from Django you want.
* Syntax not so clear.

Mongoengine
-----------

By @harrymarr!

Looks a lot like the Django ORM.

.. code-block::

    class Review(mongoengine.Document):
         name = mongoengine.CharField()

    ...

* Queries like the Django ORM.
* Super easy to develop with.
* Light schema, unenforced by db.
* django-mongonaught for admin-like functionality
* Supports *some* inter-document connections

Cons
''''

* Too structured?
* Validation messages sometimes unclear
* Lose on things like introspection (though that's what mongonaut is for)

MongoKit
--------

* Similar pattern to monogengine

.. code-block::

    class Review(Document):
        structure = {
            'title': unicode,
            'body': unicode
        }

    ...

* Queries like mongo rather than Django. Much easier to make it schemaless.
* Pretty quick.
* Types are a mix of python & mongo.
* Losing the introspection again. No schema to inspect!

Django non-rel + monogdbengine
------------------------------

* Adds NoSQL to the ORM. A Fork of django.
* Works with App Engine, MongoDB, and SQL dbs.

Pros
''''

* Exactly like normal django
* Has introspection from ``djangotoolbox``

Cons
''''

* Forks ALL of django. (1.3...). Maintenance headache potentially.
* Multidb usage is confusing
* A bit idealistic...

Summary
-------

* pymongo is low level
* monogengine is schemaless django models
* mongokit ~ pymongo++
* django-nonrel is a django fork

Thoughts: Danny
--------

* Can we build a "simple" bridge?
* What about a 3rd party app which combines standard django apps with mongo db?
  (e.g. contrib.auth, forms, social-auth etc)
* "Let's extend the django admin" doesn't work...

Why add schemas to schemaless when:

* Relational DBs
* South
* High level caching tools

allow you to do fast moving dbs easily.

Introspection tool idea:
''''''''''''''''''''''''

Immediate introspection: if there's no title then don't show a title! Treat it
like MongoDB queries.

Thoughts: Audrey
----------------

* Schemaless dbs promise performance at the expense of ACID. Lose the
  guarantees for the highter availability.
* This is OK when performance is more important than being consistend 100% of
  the time.
* Schemaless models != schemaless collections. MongoEngine is best case unless
  you need *schema anarchy*! (Props to `@harrymarr
  <http://twitter.com/harrymarr>`_ again)

Using Django with Mongo
-----------------------

* Big hurdles, but it's improving rapidly.

* Needs:

    * New tools
    * forms bridge
    * admin bridge
    * replacement for auth
    * creation of best practices

* Nothing wrong with mixing DBs.

Django mongonaut
----------------

Introspection for MongoEngine. Works so far. Want to make it independent from
mongoengine and make more generally useful.

Integrate some graphing tools? (e.g. graphviz) Should be based off immediate
introspection rather than ahead-of-time.

Summary
-------

Consider all of the tools. It's not impossible!

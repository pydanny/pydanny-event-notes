========================
Migrating The Future
========================

by Andrew Godwin

    * Works at http://lanyrd.com
    * Django core developer

It's been almost five years since South was first released, and in that time many things have changed - now it's time for a new migration system, built into Django itself and with new features and a solid foundation based on those five years of learning. Hear the problems in both running this kind of open source project as well as those of dealing with five different database backends, and how both you and South can learn from them.

Kickstarter
=============

* Wanted ₤2,500 pounds
* Got ₤17,952 pounds from 502 backers

What's wrong with South
=========================

* 5 years of learning, lessons learned
* Poor VCS branching, two people commit to same place
* Huge migration file size
* Migration sets get too large

New modules
=============

* ``django.db.migrations``

    * Migration commands
    * autodetection
    * The public API, as it were

* ``django.db.backends.schema``

    * SQL generation
    * Database abstraction
    
Databases supported

* PostgreSQL - yes
* MySQL - yes
* SQLite - yes
* Oracle - hopefully
* MSSQL - hopefully
* DB2 - maybe
* MongoDB - maybe

New migration format
=====================

.. note:: TODO get this later, the code samples are on a black backgroun.

* Shrink the size of migrationd

Dependency Management
=======================

If you and another developer both add a new migration with the same name, South sorts in ASCII sort order. Which is a serious problem if you miss a dependency

* South dependencies are driven now by a specification value in the Migration module
* Auto-Merges migrations when there is no conflicting migrations
* Can squash all the migrations into one big migration.

How is it going?
===================

Working 2-3 days a week on this full-time

Working on it:

* **Schema backends**: Mostly done, ready for merge
* **Migration code**: Still going, most complex part

Upcoming

* **Field API changes**: This Field needs to be able to inform migrations what's going on

Resources
==========

Code: https://github.com/andrewgodwin/django.tree/schema-alteration
Blog: http://aerocode.org/category/django-diaries
email: andrew@aerocode.org

Working to do this for all of us, so give him feedback!
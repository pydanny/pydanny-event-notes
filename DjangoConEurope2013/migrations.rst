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
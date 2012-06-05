===============
It's about time
===============

by Aymeric Augustin

* Django core dev
* http://static.myks.org/data/20120605-DjangoCon-It's_about_time.pdf

.. note:: Had to deal with a business thing so didn't get all of Aymeric's talk down. What I got was from some really awesome material.

RFC 3339
=========

* Current era
* Stated offset
* universal time
* instant in time

.. code-block:: python

    from datetime import datetime
    datetime(
        year=2012, month=6, day=5
        hour=16, minute=10, second-0,
        microsecond=0,
        tzinfo=FixedOffset(120)
    )
    
Time zones add complexity

aware vs naive datetimes
============================

.. code-block:: python

    >>> naive = datetime(2012, 6, 5, 16, 15)
    >>> tz = timzeone("Europe/Paris")
    >>> aware - tz.localize(naive)
    >>> naive - aware
    
From the Python docs: Whether a naive datetime object represents UTC, local time, or time in some other timezone is purely up to the program.

DST transitions
=================

.. code-block:: python

    from datetime import datetime
    
    
dates and datetimes
=====================

* dates are always naive
* they don't suffer from the same problems as naive datetimes
* using an aware datetime as a date is an accident waiting to happen
* Django supports mixing naive datetimes and dates

Django >= 1.4
==============

* Uses aware datetimes in URC internally
* stores naive datetime sin UTC in the database (except PostgreSQL)
* converts to aware datetimes in local time in forms and templates
* supports multiple time zones!

default and current time zones
==========================================

* `default` = `settings.TIME_ZONE`

    * used in models for conversions between naive and aware objects
    
* `current` = `end user's time zone`

    * used in templates and forms
    * for multiple time zones support
    
auto-conversions
==================

* ensure backwards compatibility
* avoid surprises for single time zone sites
* but support sloppy contructs e.g.,

    * filter a DateTimeField with a date
    * save a datetime in a DateField
    
Utilities
=========

.. code-block:: python

    >>> from django.conf import settings
    >>> from django.utils import timezone
    
    >>> settings.USE_TZ = True
    >>> timezone.now()
    <snip>
    
limitations in Django 1.4
==============================

* The database works in UTC (ticket #17260)
* QuerySet.dates()

    * __year/month/day/week_day

* Author of pluggable apps may have to handle two cases

Key learnings
=================

1. A datetime is a point in time. A date is a calendaring concept.
2. Use aware datetimes in UTC and convert to local time for humans.
3. learn how to use pytz properly especially `localize` and `normalize`

Time isn't as simple as it seems. Learn and practice!
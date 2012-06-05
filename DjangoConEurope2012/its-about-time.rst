===============
It's about time
===============

by Aymeric Augustin

* Django core dev

.. note:: Had to deal with a business thing so didn't get all of Aymeric's talk down.

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
    
    
    
=======================================
Class Based Views: Untangling the Mess
=======================================

by Dr. Russell Keith-Magee

    * Django Core Developer since January 2006
    * DSF President since June 2010
    * CTO and co-founder of TradesCloud

Why CBVs?
============

Introduced in Django 1.3 in 2011. What's the history?


History per 2005
-------------------

* Django is for building websites
* Views are for displaying content
* There are lots of refactorable things to do
* Generic views could handle all of this:

    * Display template
    * Display object or list of objects
    * Handle forms
    * Every view is a function
    * Configuration via arguments
    
Problems with function based generic views
------------------------------------------

* Configuration options limited by urls.py args
* No control over logic flow
* No re-use between views

.. note:: Another thing against function-based generic views was that people would implement their own broken CBV system.

Django 1.3
-----------

* They kept trying to get CBVs into Django starting with Django 1.0.

What went wrong
=================

* Fundamental confusion over purpose
* Confusion over implementation choices
* Ravioli code

    * Luke Plant described the effort as bad code.
    * "You don't know what's in the ravioli."
    * Steep learning curve

* Bad documentation

    * Russell takes the blame for the problems.
    * Myself, Marc Tamlyn, and others worked to make it work.
    
Purpose
----------

Class-Based views are an object-oriented analog for function based views.

* Class based views
* Class based Generic Views

Because we are subclassing a base class, we get tons of extra options.

* automatic OPTIONS request handling
* automatic naive HEAD request handling
* automatic HTTP 405 on unknown verbs

CB Generic Views
~~~~~~~~~~~~~~~~~~~

* Uses Class Based Views as a base
* Creates analogs of the old generic views
* Addresses limits of functional approach

Implementation Choices
--------------------------

* See details of the debate at https://code.djangoproject.com/wiki/ClassBasedViews
* A class that is instantiated as a view
* Problems:

    * What gets instantiated?
    * How does it gets instantiated?
    * Once per process or request?
    * What's the lifespan?
    * What about state? (race conditions!!!)
    * How does it work with urls.py?
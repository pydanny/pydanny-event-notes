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
-----------------

* Fundamental confusion over purpose

    * Not clear what to use it for.
    * Implementation not obvious

* Confusion over implementation choices
* Ravioli code

    * Luke Plant described the effort as bad code.
    * "You don't know what's in the ravioli."

* Bad documentation
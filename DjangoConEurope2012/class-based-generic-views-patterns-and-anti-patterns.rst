========================================================
Class-based Generic Views: patterns and anti-patterns
========================================================

* BY BRUNO RENIÉ
* CBVs added in Django 1.3

Controversy
============

Blog posts last week

* Luke Plant
* Nick Coghlan

What are views in Django?
=========================

"A view is a callable that takes a requests and returns a response"


Deprecation
=============

* Functional views are not deprecated
* Generic functional views are

Pre Django-1.3 Django CBVs
==============================

* Admin
* RSS feeds
* Sitemaps

CBV API
========

.. code-block:: python

    class View(Object):
    
        @classonlymethod
        def as_view(cls, **init):
            def view(request, *args, **kwargs):
                self = cls(**init)
                return self.dispatch(request, *args, **kwargs)
                
        # TODO find the rest
        
Declarative vs Imperative
==========================

* CBVs have a much steeper learning curve
* ccbv.co.uk is a handy resource

Usage Tips for Django CBVs
===========================

* try to keep urls.py for URL definition and nothing else
* Keep decorators in views.oy

Decorating
----------

.. code-block:: python

    # TODO show Python 2.7 version here

    class MyView(generic.ListView):
        pass
    # Complete this
    
MRO, extend, don't override
------------------------------

Unless you're 100% sure of what you're doing

Case Studies
=============

Useful recipes

Form processing
-----------------

TODO - get the form processing example

Nested Navigation
-------------------

# TODO - get example

Pagination
-----------

# TODO - get example
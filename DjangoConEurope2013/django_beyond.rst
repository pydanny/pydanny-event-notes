==========================
Django 1.6 and Beyond
==========================

By Russell Keith-Magee

    * Django core team developer
    * President of the Django Software Foundation
    * @freakboy3742
    * PhD in ...
    
This is Russell's vision for what is happening in Django, but nothing is concrete because Django is a volunteer project.

What's missing?
=================

.. epigraph::

    Good frameworks don't come from academia, they come from projects solving real problems.

    -- Jacob Kaplan-Moss

Things likely to happen
------------------------

* App Refactor

    * Application name is fixed. For example, 'coupons' in admin will retain that name.
    * What goes into an app?
    * Probably not in 1.6, maybe in 1.7.

* Schema Migration

    * South ought to be in core.
    * Andrew Godwin is working on it.
    * The plumbing is the backend, the porcelain is how users interact with it.
    
* Composite Primary Keys

    * Easy concept to explain, hard to implement with all the existing pieces.

* Increased decoupling

    * Pieces of Django core are getting moved out.
    * Local flavor is getting moved out.

* Admin 2.0

    * A lot of things it could do but it doesn't.
    * Many third-party skins
    * Current version not using CBVs but they could be.

* Release Schedule

    * Averaged a release every 11 months
    * **OMG** this means we have to update Two Scoops of Django faster. :P

* Singleton Cleanup

    * The settings a'la ``django.conf.settings``.
    * It's a problem that really needs to be fixed.
    * Considering breaking backwards compatibility.
    
Long Term Predictions (low accuracy)
------------------------------------------

* Better sharing with the rest of the Python world.

    * WSGI
    * SQLAlchemy
    * NoSQL
    
        * Probably not happening because it would only allow for a subset of the Django ORM functionality
        * What about the ORM?
    
* Extinction-level events (Django is a great framework for 2005, but it's 2013)

    * Django doesn't handle real-time.
    * Server/client separation
    
        * Javascript frameworks are not chosen yet.
        * Sourcemaps are making the debugging of compiled Javascript framework
    
    * Mobile
    
        * Objective-C
        * Java
        * HTML5
        
* How do we make great ideas happen?

    * Decisions are made to those who show up.
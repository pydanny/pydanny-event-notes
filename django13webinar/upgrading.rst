================
Upgrading Django
================

Jacob's process

#. Use virtualenv + pip
#. Upgrade just Django. Don't upgrade other things at the same time.
#. Test and pray you have real unit tests.
#. Upgrade 3rd Party Python Apps
#. Deploy
#. Start adding new features

Upgrade and Test
================

The process::

    pip install -- upgrade Django
    ./manage.py test

This is why having unit tests is a **good** thing. But also click around and test things manually.

Things to watch for
===================

    * Accessing internals: **models._meta**, **queryset.query** and other internals are not guaranteed by Django to not change. 
 
        * So if your code depends on these things they can break between versions
        * Mark this code in comments as using internals
        * write tests against this code!
        
    * Arbitrary keyword arguments: model.save(), model.delete(), signal handlers, etc can change.
    
        * Use \*\*kwargs instead of keyword arguments!
        
    * Monkeypatches
    
        * Just say no
        
    * Deprecated APIs and backwards incompatible changes (coming up next)

What about 3rd party apps?
==========================

    * The big ones should all work: South, Celery, Haystack, Tastypie, etc
    * Maybe make a sub-app or fork for those that do not.

Deploy!
=======

Get requirements::

    localhost$ pip freeze > requirements.txt
    remote$ pip install -U -r requirements.txt
    
Safety path:

 #. Build new virtualenv
 #. Grab code
 #. Build reqs there
 #. Point apache at new version of site.
 
==========================================
Having Your Pony and Committing It Too
==========================================

by Jacob Burch

    * Works for @revsys
    * Contributed to ``django.core.cache``
    * Not in AUTHORS file of Django (yet)

For many years before 2012, the topic at the tip of every argument-seeking tongue at Django Conferences was ""when is Django going to get on Github?"" Getting the core framework on the social coding site was the first stride in breaking down the barriers to having anyone and everyone not only having a pony, but getting it into core too. Now that this important step is almost a year in, just how easy is it to take the step from end-user to core-contributor? Delightfully Easy.

So easy, that I'll be breaking every rule I know in giving a talk and actually attempting to get a feature from idea, to code, to request, to a live haggle-and-debate session with core contributors in-audience, to pull request to (hopefully!) merge all within 30 minutes. Advice from a variety previous contributors on will be provided throughout the demonstration, including tips for getting very small bugs fixed quickly to strategies for getting necessary groundswell for larger full-feature ideas.


Not covered
=============

* You need to know virtualenv/git
* Large overview of Django's core code
* Advice in what to get involved in

Thoughts
=========

* It's scary to start contributing to Django
* It seems labrythine, and it is.
* It can take a while to get core code in

.. epigraph::

    Max Weber describes politics as "the slow boring of hard boards". Open source is much the same. -- Russell Keith-Magee

Confident vs Bold
========================

* Follow the wikipedia motto: "Be Bold" -- Alex Gaynor
* You are not your code -- Marty Alchin

Before you do anything with Django
====================================

* Fork Django
* ``git clone your repo``
* ``./runtestspy --settings=test_sqlite``
* Da not pass GO until tests run*


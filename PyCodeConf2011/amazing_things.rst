=============================
Amazing Things in Open Source
=============================

* by Audrey Roy
* Lots of volunteer work: PyLadies and opencomparison.org

Python community is a meritocracy
====================================

If your work has merit people use it

* Anyone can build anything
* Anyone can start a user group
* Anyone can be a leader

No permission needed
--------------------

* Just implement or emperiment with what you want/need
* Fork if necessary
* Ask forgiveness later!

It's fun
----------

* Rewarding to see your work published

Who's in charge
=============================================

You are if...

* ...you deliver code
* ...you maintain it

Decisions
---------

* Forced to make quick decisions during Django Dash
* All packages are added manually, using:

    * package name
    * PyPI URL
    * repo URL
    
* No spiders, no automation, good decision?

    * Doesn't matter, looks like it's successful
    
* Be careful of mailing lists, IRC, et all

    * don't talk too much before implementation
    * Just get something done

Your gut instinct is often right
----------------------------------------

* Django Packages

    * **Fun fact** Many of the grids were created as test fixtures and have remained
    * You can change them but keep in mind we'll track the changes and hunt down people who do wrong
    
Django
=======    
    
Why she uses Django these days
--------------------------------

* Lots of packages
* Can wire things together

Django Core vs Apps
----------------------

* Many, many batteries included
* Gives you one obvious way to do things
* Third party apps: "Django apps"
* Good

    * One pretty clear way to do things

* Bad

    * Stuck with one way to do things.
    * Example: URL routing differences

Clear pattern for Django apps
------------------------------

* Simple
* Easy to understand, implement, install
* Documented
* Repeatable

Django's Ecosystem over time
--------------------------------

* More and more new innovations implemented as 3rd-party packages
* Problem with adding all to core is then you are stuck

    * Deprecation becomes challenging
    * Additional complexity
    
Observation on Packages
============================

* Umpteen JQuery plugins
* Perl: 100K modules
* Python: 17K packages

So very useful!

Pyramid Core vs. Add-ons approach
====================================

* smaller core, more add-ons
* Anyone can write add-ons
* Some are "officially endorsed"
* Easier to do extensions of the core
* Young, but potential for rapid growth

    * Hopefully http://pyramid.opencomparison.org will help that growth

Pyramid's Ecosystem over time
====================================

* Past: Pylons, Repoze.BFG, TurboGears
* Present: small core, docs for doing add-ons - but not many yet
* FutureL Lots of add-ons!

Checklist: What 3rd Party Package Devs need
=============================================

* "Best practices" doc on how to write 3rd party packages
* Well defined, easy-to-understand spec
* Sample code (as much as possible)
* Active Community

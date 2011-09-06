==================
Read the Docs
==================

by Eric Holscher

.. note:: arrived late. :(

Intro
=====

 * launched in Django Dash 2010
 * Makes documentation hosting trivial
 * uses sphinx
 
Things you can do
====================

 * Post commit hooks on Github
 * Add custom sphinx theme
 * PDF generation via download think
 * Use their REST API for links to http://djangopackages.com
 
CNAME support 
==============

* Request for docs.fabfile.org
* docs.fabfile.org > (need to finish this out)

Architecture
============

 * Python
 * Front end caching via varnish
 
    * Varnish is the current single point of failure.
 
 * Django front ended via gunicorn and nginx

    * Docs are hosted out via nginx
 
 * Postgres SQL
 * Haystack and SOLR 
 * Chef for deployment
 * Nagios & Munin
 * CoffeeScript (*Where is the Python version? This is only in Ruby*)
 * CLI support via http://rtd.rtfd.org (**need to check this out!**)
 
Open source!
============

Pros:

    * Patches
    * People trust you most because they can see the code
    * BSD license

Cons:   

    * Known architecture information was on github
    * Early version had exposed data like IP addresses and other things
    
Hoping it makes people write more docs
========================================

 * mod_wsgi
 * django-piston
 
Lessons Learned
================

 * Think about your URLs. Really hard
 
    * Adding versions was hard

 * Lay your project out sanely
 
    * started with no tests
    * Shoved code in
    * Racked up a lot of technical debt
    * worked hard to make the project layout a bit more sane

 * Write tests!
 
    * Had a complicated code base without tests
    * They have hosted continuous integration

 * Build around a standard tool
 
    * Lots of good communication between rtfd and Sphinx
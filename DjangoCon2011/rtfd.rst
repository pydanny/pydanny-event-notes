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
===========

 * Python
 * Front end caching via varnish
 
    * Varnish is the current single point of failure.
 
 * Django front ended via gunicorn and nginx

    * Docs are hosted out via nginx
 
 * Postgres SQL
 * Haystack and SOLR 
 * Chef for deployment
 * Nagios & Munin
 * CoffeeScript (Where is the Python version? This is only in Ruby)
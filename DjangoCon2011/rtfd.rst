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
 
CNAME support 
==============

* Request for docs.fabfile.org
* docs.fabfile.org >

Archiectrure
==============

 * Python
 * Front end caching via varnish
 
    * Varnish is the current single point of failure.
 
 * Django front ended via gunicorn and nginx

    * Docs are hosted out via nginx
 
 * Postgres SQL
 * Haystack and SOLR 
 * Chef for deployment
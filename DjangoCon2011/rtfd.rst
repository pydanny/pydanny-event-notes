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

What makes it work
===================

 * Django
 * Python
 * Post commit hooks
 
Things you can do
====================

 * Add custom sphinx theme
 * PDF generation via download think
 
CNAME support 
==============

* Request for docs.fabfile.org
* docs.fabfile.org >

Archiectrure
==============

 * Front end caching via varnish
 * Django front ended via gunicorn and nginx

    * Docs are hosted out via nginx
 
 * Postgres SQL
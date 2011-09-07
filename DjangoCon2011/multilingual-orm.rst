==================================
Making the Django ORM Multilingual
==================================

By Jonas Obrist

 * Lead of the django-cms project: https://django-cms.org

What this is all about
=========================

 * Models
 * The ORM
 * Admin
 * Forms
 * not gettext!
 
Que?
======

 * Because you may not understand this title!
 * You might lose customers and users

What does he want
==================

 * Multilingual content in the database
 * Editable in a usable admin inteface
 * Easy, Django-like API
 * Good performance
 
    * Most of the existing tools are slow
    * Bad performance
    
State of now
=============

 * 10 packages at http://djangopackages.com/
 * No consensus on how this should be done
 
    * API
    * Base solutions
    * many ideas floating around
    
Approaches
===========

 * 1 table, 1 extra field
 * 1 extra table with key/value translations
 * 2 tables, one for translated fields one for translated fields (dual-table) - **How I've done it**
 * Translations serialized into a single field (Pickle/JSON) - **No search without a ton of hacking!!!**
 * gettext
 * Google Translate
 
    * This is not a serious service for a real project
    * Third party and relies on Google management
    
Single Table Approach
======================

Pros

 * Somewhat easy
 * few queries
 * fallbacks
 * Hard to implement filtering
 
Cons

 * Multisite this falls apart. Doesn't work
 * Migrations are painful because each language requires a schema migration
 * Size of query result can get big
 * Hard to make nice admin
 * Hard to handle required fields
 
Example::
 
.. sourcecode:: sql

    select book.isbn, book.title_en, book.title_de from book;
    
Dictionary Table Approach
==========================

Pros

 * Easy to implement
 
Cons

 * No filtering
 * No sorting
 * Admin
 
No example cause the Query is too big

Two Table Approach
=====================

Pros:

 * Can be made very fast
 * few queries
 * Works with south
 * makes sense
 * possible but hard to make nice admin
 
Cons:

 * Hard to implement
 * joins
 * Usually done with bad performance **I addressed this with caching and celery**
 * Incompatible with lots of other packages (requires custom queries unless you are really careful)
 
Common problems
================

 * Admin doesn't like new ideas
 
    * `django.contrib.admin.validation` is a blocker
    * Extensible but not customizable
    * Forms are a weak spot in Django, and Admin uses them in a really odd way
 
 * ORM just wasn't written to be extended, was written to be used
 
    * Relations: Starting model controls everything
    * Not intended to be changed
    * Nice things: `QuerySet.iterator`
 
 * Performance issues on all of them
 * Usually written under time pressure (deadline)
 * Many packages are undocumented and lack tests

Summary: The Situation
========================

 * Translatable models are hard
 * All available solutions have their problems
 * Maybe something needs to be done in Django
 
What could Django do?
---------------------

 * Do nothing
 * Provide hooks/APIs to make this easier
 * Provide support for translated models
 
If Django does nothing
-----------------------

 * List of multilingual libraries grow
 * Many custom undocumented implementations 
 
If Django adds new APIs
-----------------------

 * Probably too low-level
 * abstract solutions add overhead

Django adds multilingul support
----------------------------------------------

 * Bikeshedding potential
 
    * What approach to take?
    * What API should look like?
    
 * Easiest way to implement
 * Could be done backwards compatible
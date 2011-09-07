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
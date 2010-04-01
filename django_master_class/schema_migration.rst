================
Schema Migration
================

Keeping your sanity when changing models

Gems
----

 * You don't need to use Django tools to do it. Consider sqlalchemy-migrate
 * Question: Will South get brought into core? Not until more thought has been given and products mature nicely.

The problem with the Django ORM
-------------------------------

 * manage.py syncdb doesn't alter tables
 * manage.py reset just deletes tables
 * SQL Shell doesn't record any changes.
 * SQL scripts are problematic
 * Forgetting migrations!
 * Track migrations
 * Need to be able to go forwards and backwards
 * Keep multiple developers in sync, just like good source control
 
The main lesson
---------------

 * You have to have a tool
 * Once started, you always have to use the SQL tool

Django Migrations Tools?
------------------------

 * Nothing in core
 * options Jacob knows about
 
   * deseb
   * django-evolutions
   * dmigrations
   * migratory
   * south
   * yadsel
   * sqlalchemy-migrate looks good.
   
Django-Evolutions
-----------------

 * About 2 years old
 * Works with **syncdb**
 * Applies (some) evolutions automatically. Kind of terrifying!
 * Write evolutions in Python or SQL
 * Requires some care in workflow especially in a team
 * Lead by Django core contributor (Russ Keith-McGee)

South
-----

 * 1 year old
 * disables syncdb; migrations from the start
 * supports auto-generation
 * Python only
 * works for data migrations
 * good for teams
 * At this time is the recommended system.
 * South lets you control dependencies 
 
   * http://south.aeracode.org/wiki/Dependencies
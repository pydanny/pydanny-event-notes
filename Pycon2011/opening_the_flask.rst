========================================
Opening the Flask
========================================

by Armin Ronacher

April Fool's Joke
=================

Decided to mock the various microframeworks:

 * web.py
 * bottle
 * web2py
 
Features
--------

 * Eirik Lahavre
 * Entirely made up
 * "Impressive scaling capabilities"
 * one file framework
 
What he learned
---------------

* people took him seriously
* marketing beats quality
* features don't matter
* people aren't looking at source code
* Does not have to be new

Inspiration
===========

* be honest
* don't reinvent things
* stay in touch with others


Details
================

* jinja2
* wuerkzueg
* optionally blinker for signaling
* tons of documentation
* "best of breed" code

Some numbers
------------

* 800 LOC
* 1500 LOC tests
* 200 A4 Pages of Documentation

Ecosystem
----------

* Over 30 extensions
* very active mailinglist
* over 700 followers and 100 forks on github - yay

Design Decisions
-----------------

* use of Context Locals as globals

    * Rather than pass around the request object you can see it everywhere
    
* No import time side effects
* Explicit application setup

    * Applying WSGI middlewares
    * more than one app
    * testing
    * create app in function
    
* circular imports
* cached imports
* keeps things simple

Extensions
-------------

* Formal extension system
* Approval process
* Core must stay small so extensions must work with core

Lessons Learned
------------------

* Documentation matters

    * Use a clean documentation style and people will help document more
    * Documentation style for extensions
    * Simple visual design

* Communication matters
* Heartbeat signals
* Consistency
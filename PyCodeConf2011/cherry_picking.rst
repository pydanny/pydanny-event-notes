================================
Cherry-picking for Huge Success
================================

* by Armin Ronacher
* @mitsuhiko
* Part of the Pocoo team
* Guy behind flask, jinja2, much more

Preface
========

* Doesn't care about language fights
* Use the best tool for the job

Consider Twitter
=================

* 2006: off the shelf Rails application, static HTML, basic XML API
* Now: The API is the service. Website itself is a JavaScript app. Scala/Erlang backend

Does this mean Ruby sucks?
=============================

* Not it does not
* Neither does Python
* Ruby / Python are amazing for prototyping
* Expect applications to change and grow in implementation over time

Proposed Solution
====================

* Build smaller apps
* Combine apps to make bigger apps

Cross boundaries
--------------------

* Pygments is awesome
* Need Pygments in Ruby

    * A: rewrite in Ruby
    * B: Use different syntax highlight
    * C: Use pygments as a service called by Ruby
    
"It only does Django"
------------------------

* You wrote a library that does something useful (thumb-nailing for example)
* Don't make it depend on Django if you can help it
* Try to make it independent
* Then implement a separate Django app that calls your tool

.. note:: This also happens with the Zope community. They did "Zope Only Projects" first. ;)

Protocol Examples
==================

Flask Views
-------------

* Wiews can return response objects
* Respons eobjects are WSGI apps
* no typecheck
* Return any WSGI app
* WSGI server doesn't care if it

Difflib + Genshi
----------------

* Genshi is valid XML
* Difflib returns a string
* Change Difflib to be `<ins>/<del>` so Genshi can render it
* Instant pages!

Serializers
-------------

* pickle, phpserialize, itsdangerous, json
* Within the compatible types it 

Loosely couple all the ways!!!
====================================

Many small bits with specific merge points that are loosely coupled

* WSGI
* HTTP
* ZeroMQ
* Message queues
* Datastore
* JavaScript

WSGI
====

* Dictionary passed around
* Framework independent, but only for Python
* Tornado and Twisted don't do it, but everything else does
* Middlewares are unused and hard to make

    * TODO: Get his middleware example for use as possible sub-domain hack
    
* WSGI middleware has issues:

    * Can't consume dform data
    * Processing response from application is complex
    * Can't inject HTML 
    * TODO - last bullet?
    
* Libraries

    * Werkzeug
    * WebOb
    * Paste
    
Django & WSGI
------------------

* Django used to do WSGI badly
* Getting documented 

HTTP
====

* Pure HTTP is more work than WSGI
* Easily debugged
* Language independant
* Need syntax highlighting with Pygments but your project is Ruby?
    
    * Write small Flask app that exposes Pygments as a service
    
Libraries
------------

* Python-Requests
* TODO
* TODO


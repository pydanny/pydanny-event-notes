===========================
Fractal Architectures
===========================

by Laurens Van Houtven

An alternative take on Django's traditional layered web service architecture.

.. note:: Was very late.

Concept
=======

Use many tiny servers with tiny Twisted powered web servers with tiny instances of SQLite3 as the backend. Each user gets their own mini-server!

Backend
=========

Twisted
--------

Cause he's a core dev and is asynchronous

SQLite3
-------

* It's in the Python stdlib
* Wrapped by Axiom, a Python library, documented at http://lvh.com/axiombook
* Using SQLite3 means it's the same development environment as production - because how for developers PostgreSQL is **NOT** set up the same locally as production.

Static Assets / Long term storage
--------------

* Uses a CDN like AWS or something else. 
* Good for handling of micro-instance failure
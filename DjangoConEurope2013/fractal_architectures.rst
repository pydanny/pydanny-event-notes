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

Cause he's a core dev and is asynchronous. We could use Django.

SQLite3
-------

* It's in the Python stdlib
* Wrapped by Axiom, a Python library, documented at http://lvh.com/axiombook
* Using SQLite3 means it's the same development environment as production - because how for developers PostgreSQL is **NOT** set up the same locally as production.

Static Assets / Long term storage
--------------

* Uses a CDN like AWS, OpenStack Swift, or something else. 
* Good for handling of micro-instance failure

Two Ways for Better Performance
================================

* Do less stuff
* Make stuff run faster

If you off-put stuff from one server onto a database server, cache server, et al, then even in-database center latency will become an issue. His approach is to put everything on one tiny server per user and reduce latency between machines to **nothing**.

This is the concept of **Data Locality**.

Devil's Advocacy
=================

* Unusual design might make it hard to get more developer help.
* Weird separation. 
* Data is weird, maybe not good for big data. But 99% of sites don't have actual big data.
* Transaction support doesn't work.
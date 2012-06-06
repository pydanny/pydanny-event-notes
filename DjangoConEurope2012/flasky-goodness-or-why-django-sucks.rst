=============================================
Flasky Goodness (or Why Django Sucks?)
=============================================

by Kenneth Reitz

* http://twitter.com/kennethreitz
* Works for Heroku

Hos Open Source work
==========================

* http://python-guide.org

    * Documented best practices
    * Guidebook for newcomers
    * Reference for seasoned veterans
    * Don't panic & always carry a towel

* http://python-requests.org

    * HTTP for humans

* http://httpbin.org

* legit: Git workflow for Humans
* Envoy: Subprocess for Humans
* Tablib: Tabular Data for Humans
* Clint: CLI App Toolkit
* Autoenv: Magic Shell Environments
* OSX-GCC Installer: Provokes Lawyers

Open Source All The Things!
============================

* Components become concise and decoupled
* Concerns separate themselves
* Best practices emerge
* Documentation and tests become crucial
* Code can be released at any time
* Abstraction

Let's build something
========================

Why pick Django?

* Makes modular decisions for you
* Makes security decisions for you
* Excellent documentation
* Installable third-party Django apps
* Tremendous resources & Community
* much more cause anything is possible!

Django Application
======================

* Tools & Utilities

    * Management Tools
    * Supporting Services

* Web Process

    * User Interface
    * API
    * Data Persistence
    * CRUD Admin
    * Authentication
    
* Worker Process

    * Deferred Tasks
    * Scheduled Tasks

Single Codebases are great
============================

* All the benefits of the Django stack
* Figure out architecture as you go
* Shared modules keep you dry
* Make broad, sweeping changes
* Only need to deploy once

Single codebases are EVIL!
==============================

* Tight coupling of components
* Broad tribal knowledge required
* Iterative change of components difficult
* Technical debt has a tendency to spread
* Forced to deploy everything at once.

Anything is possible... but that ends up with a monolithic application.

CONSTRAINTS FOSTER CREATIVITY
===============================

* Having rules gives you an environment in which to play.
* Text Editors vs IDEs (Vim lets you do so much, Sublime Text limits what you can do)
* Prime vs Zoom Lenses
* Mac OS X vs Desktop Linux
* Pen/paper vs electronic notes

Build for services
====================

* Components become concise & decoupled
* Concerns separate themselves
* Best practices emerge
* Documentation and contracts become crucial
* .. note:: missed some here

**Results in composability**

QUESTION: SOA often is a nightmare because of lack of Documentation and contracts. When that happens how do you deal with that?

Django: For API Services
=============================

* Significant boilerplate code for simple views
* No need to templates, tags, etc
* API Libraries are buggy; could use some love
* if ``request.method == 'POST'``

Django: For API Consumer
=============================

* Keep in mind, database is handled by the API
* Makes modular decisions for you
* Deals with the database for you
* Installable third-party Django apps

Enter Flask
=============

* HTTP Web Framework based on Werkzeug
* Excellent for building web services
* Elegant and simple

Flask Familiarities
====================

* WSGI Application Framework
* Jinja2
* activity community
* Started an April Fool's joke
* Just 800 lines of code
* Heavily tested, 1500 lines of tests
* Exhaustively document; 200 pages of docs
* Layered API; built on Werkzeug, WSGI

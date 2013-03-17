=================================================================
Dynamic Code Patterns: Extending Your Applications with Plugins
=================================================================

Python makes loading code dynamically easy, allowing you to configure and extend your application by discovering and loading extensions at runtime. This presentation will discuss the techniques for dynamic code loading used in several well-known applications and weigh the pros and cons of each approach.

by Doug Hellmann

The applications studied include:

* Mercurial
* Sphinx
* Trac
* virtualenvwrapper
* Django
* nose
* ceilometer
* OpenStack CLI
* cliff

How plugins work?
===================

Discovery
-------------

* File/Explicit: Mercurial
* File/Scan: Diamond/Blogofile
* Import reference / Explicit: Django, Mercurial, Pyramid, Spginx, Nova
* Import reference / Scan: 1 or 2

Enabling 
-------------------

* Explicit: Django, Pyramid, SQLAlchemy, Blogofile, Mercurial, Trac, Sphinx
* Implicit: virtualenvwrapper, cliff


Importing
----------------------

* Custom: Django, Pyramid, Sphinx, Diamond, Nova, Nose, SQLAlchemy, Blogofile
* pkg_resources: Trac, Nose, SQLAlchemy, Blogofile

API Enforcement
------------------------------------

* Convention is easier but Base Class / Interface is more stable
* Doug used Abstract Base Classes for cliff

What Doug did for cliff
========================

Discovery / Importing 
------------------------------------

* Entry points
* Be consistent

Enabling
---------

* Explicit disabling
* Automatic disabling

Summary: Everything is turned on by default.

Integration
-------------

* Fine
* Inspect
* Application owns relationship

API enforcement
-----------------

* Abstract base Classes
* Duck Typing
===============================
Python Web Summit March 8, 2012
===============================

* Hosted by

    * Michael Ryabushkin
    * Chris McDonough

* url: https://us.pycon.org/2012/community/WebDevSummit/

Introduction
=============

**by Michael Ryabushkin**

How did this start?
--------------------

* People::

    Chris McDonough
    Mike Orr
    Phil Jenvey
    Mike Bayer
    Danny Greenfeld
    Audrey Roy


During the summit
-----------------

* Panels are important, but take people aside if need be



Creating a Better Deployment Story
=====================================

**Moderated by Jacob Kaplan-Moss (Django DBFL)**

Panelists:

* Tarek Ziadé (Distribute/Packaging)

    * has to play namespacing games to make sure that we get to use DistUtils backporting across versions of Python
    
* Nate Aune (DjangoZoom, Appsembler)

    * All tools (Plone, Django) makes it hard to do deployments. Hence his deployment startups (DjangoZoom and Appsembler).
    * We need to come up with a standard and insist on using it.

* Kenneth Reitz (Heroku)

    * pip needs to be able to set versions of Python
    * PyPI needs more attention

* Ian Bicking (Paste/WebOb/Silver Lining)

    * Let's create a formal Application Package specification.
    * Problem to overcome is the difference between developers and sys admin

* Jim Fulton (Buildout/Zope)

    * Company does development and maintains 500 applications
    * "Packaging needs to be better so we can deploy more easily."


Questions
---------

#. How come Java .war files do it better than Python?
#. What is the status quo?
#. What are people working on to make this better?

Formal Application Package Specification?
------------------------------------------

Ian Bicking's thought on how to do it. Would have these things::
    
    Formal path specification
    Formal dependency listings
    Project description
    Python version labeling
    Include non-Python components (database, libraries, etc)



Porting to Python 3
====================

Moderated by Barry Warsaw (Canonical, Python FLUFL)

* Guido van Rossum (Python)
* Mike Bayer (SQLAlchemy/Mako)
* Robert Brewer (CherryPy)
* Armin Ronacher (Flask)
* Chris McDonough (Pyramid/WebOb)


Factoring Code for Reuse
========================

Moderated by Danny Greenfeld (`consumernotebook.com`_)

* Tres Seaver (Zope/CMF/Pyramid)
* Mariano Reingart (Web2Py)
* Alex Gaynor (Django/PyPy)
* Michael Foord (IronPython, Mock)
* Carl Meyer (Virtualenv, Pip)

.. _`consumernotebook.com`: http://consumernotebook.com


"State-Of" Multi-Talk Round 1
==============================

Each of these speakers, a leader in their field, gets time to talk about his subject.

* Graham Dumpleton (WSGI 2 ideas)
* Benoît Chesneau (gunicorn)
* Ben Bangert (Pylons Project)
* Robert Brewer (CherryPy)

Promoting Python for Web Use
=============================

Moderated by Paul Everitt (Pyramid)

* Steve Holden (PSF/DjangoCon)
* Liz Leddy (Plone/PloneConf)
* Eric Holscher (`Readthedocs.org`_)
* Leah Culver (`Grove.io`_)
* Danny Greenfeld (`consumernotebook.com`_)

.. _`Grove.io`: http://grove.io
.. _`Readthedocs.org`: http://rtfd.org
             

"State-Of" Multi-Talk - Round 2
=================================

* Glyph Lefkowitz (Twisted)
* Jannis Leidel (Django Project)

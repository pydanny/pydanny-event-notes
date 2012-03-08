===============================
Python Web Summit March 8, 2012
===============================

* Hosted by

    * Michael Ryabushkin
    * Chris McDonough

* url: https://us.pycon.org/2012/community/WebDevSummit/

.. note:: Taking notes on a panel is really challenging. Apologies on whatever or to whoever I miss.

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

    * New distutils lets you specify versions of third-party packages. But... redhat and other OS tools have their own package names. Ugh.

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
#. How do we make it so that Python is as easy to deploy to the web as PHP.
#. What is the status quo?
#. What are people working on to make this better?

Formal Application Package Specification?
------------------------------------------

Ian Bicking's thought on how to do it. Would have these things::
    
    Formal path specification
    Formal dependency listings
    Project description
    Python version labeling
    Include non-Python components (database, libraries, fortran, etc)
    
Jacob's comment: Is this going down the route of Chef/Puppet?

Namespacing Distributions
---------------------------

* Tarek as to play namespacing games to make sure that we get to use DistUtils backporting across versions of Python.     

* Armin Ronacher commented: "*The fact that having the same package name for distutils2/packaging would be a problem shows the root of the issue: no proper version deps.*"

Takeaways
---------

* Force deployed applications be a package.
* Formal application specification?
* Specify Python versions in virtualenv/buildout
* The challenge of dealing with vendor named projects
* Jacob is going to publish a specification that will hopefully get the community moving. And he invites others to participate on his work.

    * The others pledged to help out or work on best practices.


Porting to Python 3
====================

**Moderated by Barry Warsaw (Canonical, Python FLUFL)**

* Chris McDonough (Pyramid/WebOb)
* Armin Ronacher (Flask, Jinja2)
* Guido van Rossum (Python)

    * I don't know much about how you guys do Python web development and want to know so I can make it easier for Python 3 conversions.
    * There was artificial ambiguity introduced in Python 2 in regards to strings.

* Mike Bayer (SQLAlchemy/Mako)

    * The Python database API needs some love. I agree in that a huge, unmentioned hurdle for Python three are other libraries besides web frameworks and unicode. DBAPI, PIL, etc.
    * PEP 249 doesn't mention unicode. http://www.python.org/dev/peps/pep-0249/

* Robert Brewer (CherryPy)

Questions
---------

* Chris McDonough: Who runs web apps on Python 3?: crickets
* Barry: What are the big blockers
* Me: What about auxiliary library blockers like PIL, lxml, DB-API?

    * Answer: http://stackoverflow.com/questions/3896286/image-library-for-python-3
    * Answer: https://github.com/gpolo/pil-py3k
    * Answer: https://github.com/sloonz/pil-py3k
    * Answer: http://www.lfd.uci.edu/~gohlke/pythonlibs/#pil
    * Answer: http://www.imagemagick.org/download/python/
    * ..note:: Pillow does not solve the Python 3 issue

Compelling arguments for Python 3
----------------------------------

* Armin: Python 3 has some powerful features for sockets and other components that Python 2.x lacks.
* Barry Warsaw: Newer and more powerful libraries being written in Python 3.


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


Quotes
=========

"Django isn't a functional unit. You include it and it just sits there."

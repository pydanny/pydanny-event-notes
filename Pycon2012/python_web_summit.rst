===============================
Python Web Summit March 8, 2012
===============================

* Hosted by

    * Michael Ryabushkin
    * Chris McDonough

* url: https://us.pycon.org/2012/community/WebDevSummit/

.. note:: Taking notes on a panel is really challenging. Apologies on whatever or to whoever I miss. Any misquotes are my fault and not the fault of the speaker.

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
    * .. note:: Pillow does not solve the Python 3 issue
    
* Dylan Jay: Why are library writers having to maintain two copies of their library code?

Compelling arguments for/on Python 3
-------------------------------------

* Armin: Python 3 has some powerful features for sockets and other components that Python 2.x lacks.
* Barry Warsaw: Newer and more powerful libraries being written in Python 3.
* Wayne Witzel: Give a ton options for porting to python3, they won't choose any of them. Most people just want to be told what is right.
* Barry Warsaw: 2-to-3 tool is useful for getting started, but once in the weeds I find that I dive into the code.


Final Thoughts
---------------

.. note:: my summary of their statements.

* Chris McDonough: We need to make people more enthusiastic about Python 3.
* Armin Ronacher: Improve the guides on porting.
* Guido Van Rossum: This will be resolved. It's going to be a while, but we can make it. We'll remember how hard it was to move forward to Python 3.
* Mike Bayer: This will be resolved when we think in Python 3 by default. And make Python 2.x a boring backport.
* Robert Brewer: 


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

Graham Dumpleton (WSGI 2 ideas)
----------------------------------

* PEP 333 was created back in 2003
* PEP 3333 was created back in 2010
* Wanted something better:

    * Make it simpler
    * standardized high level request/response objects
    * Async support (not possible because so different)
    * Resource management
    * Unknown request content length
    
        * no compressed request content
        * No chunked requests
        * no full duplex HTTP

* Has the boat sailed?

    * Too much legacy code relying on WSGI 1.0
    * Missed opportunity with Python 3
    
* Graham's ideas:

    * use context managers to improve resource management
    
        * need to override close() of the iterable
    
    * Implement wsgi.input as an iterable
    * TODO add what I missed

Benoît Chesneau (gunicorn)
----------------------------

The state of gunicorn:

* First commit was November 30, 2009, Three users at first
* preform model
* Thread-safe
* Automatic worker process management
* Manage using signals
* Natively support WSGI, Django, Paster
* HTTP streams: decode on the fly http chunks
* Supporting sendfile & FileWrapper
* Simple Python configuration
* Multiple workers (sync and async)
* Various server hooks
* use your own logger
* Some issues:

        * Reload - graceful (HUP) or reexec (USR2)
        * The Django case: python-manage.py
        * Performance issues due to WSGI
        * CGI compatibility: headers
        * CONTENT_TYPE,CONTENT_LENGTH,SCRIPT_NAME
        * The WSGI spec needs to be completed

    * Async workers & blocking issues

        * IO access like the filesystem are not greened
        * C drivers
    
    * Web app configurations & deployment: we need a standard

* Challenges:

    * Python 3
    
        * the case of sync workers
        * Handle extensions/plugins
        
    * New needs on the web: websockets, SPDY
    * modular HTTP & WSGI server in Python

 
Ben Bangert (Pylons Project)
------------------------------

State of the Pylons Project:

    * Lots of community plugins developing
    * Larger frameworks on top taking off along with bootstraps
    * Ploneconf Pyramid track
    * 62 reports, 31 devs with commit
    * lots of ``pyramid_*`` packages
    
Challenges

    * Porting to Python 3 (is doing very well)
    * organizing and simplifying sometimes overly pedantic documentation
    * TurboGears
    
        * Still exists
        * Some progress on community migration
    
    * Standardizing deployment
    * Foundation efforts
    * Pylons conf (189 members of the SF Bay Pylons meetup)
    * Increasing presence at conferences (not just Python ones)
    * More awareness of professional support
    * Moar books?


Robert Brewer (CherryPy)
------------------------------

State of CherryPy

    * It works in Python 2.7x
    * It works in Python 3.x
    * Being broken up into modular components so the WSGI HTTP server can be used in things like Pyramid

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

Glyph Lefkowitz (Twisted)
---------------------------

* It works for the web!
* Lots of cool features
* Works more as a container rather than a platform.
* Has excellent support for Windows. Has an MSI, Executable, etc
* Needs to fight the impression of being a giant library. It is actually small.

Jannis Leidel (Django Project)
--------------------------------

* Used in a lot of places around the world in small and gigantic projects
* 21,700 user list
* 7,000 developer list
* 33 committers
* 2,5000 downloads/day
* 2,100 projects on PyPI
* Django 1.4 almost out

    * New project layout
    * Custom project templates
    * Standard ``WSGI`` entrypoint
    * Full timezone support
    * In browser testing
    * Cookie session backend
    * Clickjacking protection
    * New form wizard
    * i18n URLs
    
New orm functions:

.. sourcecode:: python

    select_for_update()
    bulk_create()
    distinct('filename')

Quotes
=========

"Django isn't a functional unit. You include it and it just sits there."

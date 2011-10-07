===================================
API Design and Pragmatic Python
===================================

* by Kenneth Reitz
* Works for readability.com
* Used to work for changelog
* loves open source
* Author of requests and tablib libraries

.. note:: Kenneth's mic kept going out. Hope all his words are captured!

Alternative Titles?
======================

* Python is a Ghetto 
* Python Jumped the Shark
* Python for Humans!

His libraries
==================

* Requests: HTTP for humans
* Tablibs: Pythonic Tabular Datasets
* legit: Awesome Git Interface
* OSX-GCC-Installer (angers lawyers)
* Clint: Command-line Interface Tools
* Httpbin.org: Request & Response Server

Philosophy
========================

We share a dark part:

 * PHP
 * Java
 * ColdFusion
 
We all love the Zen of Python::

    >>> import this
    
Bits:

* Beautiful is better than ugly
* Explicit is better then implicit
* Simple is better than complex
* If the implementation is hard to explain, its a bad idea (unless you are PyPy)
* There should be one and only one way to do things

HTTP as an example of API issues
=================================

Github API client in Ruby
-------------------------


TODO: Get Ruby example from his slides. Ruby makes this easy

Github API client in Python: Ugh
----------------------------------

 * Pick the right std lib http/url/lib/2
 
TODO: Show the the example Python code from Confessions that I stole from Kenneth. :)

TODO: Show his example from trying to hit a private repo

Admit it
-----------

* If this were you coming into Python, you would leave and not come back
* THis is a serious problem

urllib2 is toxic
-----------------

* Over-engineering
* Makes the simple/trivial hard
* Hard to debug
* Hard to test

Solution
---------

* Python needs more pragmatic packages
* Pragmatic means implementation without focusing too much on thoery
* Figure out the actual reqs 

Contention
----------

 * If you have to revisit docs every time to use an API the API is bad
 * 
 
Subprocess
===========

* Powerful
* Effective
* Second worst stdlib module ever

Solution
-----------

* **envoy**
* Replaces/wraps Subprocess

File and System Operations
============================

* sys | shutils | os | os.path | io
* Really difficult to run external commands
* The blocks dev+ops guys from wanting to use Python

Installing Python
===================

* Installing Python
* Decisions, Decisions (Binary, Homebrew, 32 bit, Macports, Source, what?!?)
* What happened to just one way to do it?
* Pain on Mac, Windows

XML 
====

 * `etree` is terrible
 * `lxml` is awesome, but difficult to install

Packages and Dependencies
============================

* pip and easy_install?
* setuptools not inclued with python?
* Distribute?
* No easyt_uninstall

Date[time]s
============

* datetime, time, calendar? Which one?
* What third-party libraries are around

Unicode
=========

* Kenneth says it's a simple problem
* Maybe the core docs should have an easy-to-find good description? Am I missing something?

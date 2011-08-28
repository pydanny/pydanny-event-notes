================================================
Asynchronous and Evented programming in Python
================================================

*With Rocks In*

by Aurynn Shaw

* Works at WETA Digital
* https://github.com/aurynn
* She likes shiny things

Not really covering Tornado

Introduction
============

* Much ado about Node.js
* Event driven!
* Tornado, from facebook
* Lots of buzzwords
* Async is '*sort of*' doing two things at once

Threading
==========

Really awesome until you hit issues like:

* Locking
* Shared state is hard
* Even experts have problems with it

Multiprocessing
===============

* Let the kernal care
* Easy to write MP code on unix-likes
* Can even go multi-system

Problems

* Hard to share data
* import multiprocessing can be... quirky

Asynchronous is hard
======================

* **You have to let go**
* Bending your mind to the Async way is still hard
* A single mistake can hang
* Probably going to be slower

So really, what is async?
==========================

* The core of async is the event loop.

    * Basically a while loop running
    * Checks for events
    * Events are pretty generic
    * In Twisted they have to be callbacks
    
* But once the code is in the loop, **you have to let go**.

    * Once the code is in the loop it can slow everything down
    * Your functions have to be as small as possible
    * Keep data/functions/etc really tiny
    
Async code is hard
===================

* functions don't work anymore - you are working with **Deferred**'s
* Most APIs built on twited return Deferreds


.. sourcecode:: python

    
    from twisted.internet import defer
    
    df = defer.Deferred()
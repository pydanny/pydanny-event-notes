================================================
Asynchronous and Evented programming in Python
================================================

*With Rocks In*

by Aurynn Shaw

* Works at WETA Digital
* https://github.com/aurynn
* She likes shiny things


.. note:: This talk not really covering Tornado


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
        
        * should do this anyway
    
Async code is hard
===================

* functions don't work anymore - you are working with **Deferred**'s
* Most APIs built on twited return Deferreds

.. sourcecode:: python

    from twisted.internet import defer
    
    df = defer.Deferred()
    
    def gotARequest(request, response):
        df = conn.query('select * from user;')
        df.addCallback(_someData, response)
        df.addErrback(_someError, response)
        return df  
        
    def _transform(rows):
        # rows here is now the returned data
        return [my_object(row) for row in rows]
        
    def _someData(rows, response):
        response.render(rows)
        response.finish()
    
This is how you fire off things:

* `.callback` starts the callback chain
* `.errback` causes the callback chain to explode and die messily


Synchronous Example of same thing
==========================================

.. sourcecode:: python

    def my_functZ(request, response):
        rows = conn.query('select * from user;')
        # This will hang until DB gets back to us
        return response.row(rows)

Asynchronous != faster
======================

* Not actually faster
* The event loop is overhead
* The event loop is overhead without proper coding

So why do this?
=================

Aurynn says: 

* Scales beautifully
* Terribly elegant (not sure I agree with this - need to try it)
* closer mapping to reality

What about Tornado?
====================

* Event loop + web framework
* uses inline callbacks

Incomplete code example:

.. sourcecode:: python

    def my_func():
        def rows(results):
            for res in results:

So why Tornado over Twisted
============================

* Supposedly faster

    * Aren't performance tests biased?
    * Tornado's benchmarks are on extremely insignificant tasks. Literally "Hello, World".
    * Twisted does have libraries to interact with real blockers like:
    
        * AMQP
        * IMAP
        * POP
        * PostGres
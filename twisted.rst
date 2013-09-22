==================================
Using Twisted with Everything Else
==================================

by LVH

Why should you care about Twisted?
===================================

* Async before it was cool!
* IRC, SMTP, DNS, SSH, Websockets
* Time events, sane process and thread management
* Protocol and transport abstractions
* Twisted vs Django, Flask, et al

    * Incoming e.g. a chat server
    * Outgoing e.g. a scraper

Prereqs for this talk
=======================

* Python
* Possibly Twisted

How Twisted Works
==================

* Reactor

    * Object

        * Register new events
        * Waits for events
        * Dispatches them when they occur

    * Internally an event loop

        * Except for test reactors e.g. clock
        * backed by some event mechanism

* Reactor Interfaces (usually call higher-level APIs)

        * IReactorBase: run, stop
        * IReactor(TCP|IDP|SSL|Multicast|UNIX|etc)
        
* Deferreds

    * An object that you get now
    * Gets you a result (or failure!) later
    * Very flexible
    * Used because operations take time now and you can't always get a response right now
    * Blocking API

        * Evaluate or raise some point in the future
        * Thread can't do anything else in the meantime

    * Deferrred API

        * Get an object representing the future result right now

SOA - Service Oriented Architecture
=====

* Loosely coupled things that talk to each other
* Components written in Python, Cobol, 
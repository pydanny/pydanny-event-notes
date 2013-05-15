====================================
Circus: process & socket manager
====================================

* By Tarek Ziade

    * Works for Mozilla
    * 

Circus is a process manager we developped at Mozilla while working on high scalability, we wanted to have a way to deal with our processes directly from python, and in a better way that's what possible with the standard library.

Circus uses zeromq in its internals, and thus is easily extensible. We'll present you how you why we built circus, how to use it and some core concepts that were useful in the conception of the tool. Also, we'll demonstrate how easy it is to plug circus with a Django stack.

Typical Django Deployment
==============================

* Nginx > Gunicon > Django + sentry + celery


Supervisord is frequently used for management of these components. Alternatives include:

*  Bluepill (less mature)
* upstart (system level - root access needed)
* daemontools (low-level like upstart)
* got, monit, runit, etc.

Missing features from supervisord
==================================

* Realtime stdout/stderr
* realtime stats
* powerful web console
* Remote access
* clustering
* event-based plugins

Since those were missing, Tarek launched his own project: Circus!

Technical choices for Circus
=============================

* Python 
* PSUTIL
* ZeroMQ
* TODO - get rest of this

The Core: psutil
==================

Third-party library that is easy to use and pretty elegant:

.. code-block:: python

    >>> import psutil
    >>> p = psutil.Process(7384)
    >>> p.name
    'Address book'
    
    >>> p.uids
    user
    
The Messenger: ZeroMQ
======================

* async library for message passing == smart socket
* highly scalable
* transports: ITC, IPC, TCP, PGM (multicast)
* principal patterns

    * request
    * pub/sub
    * push/pull

* used by IPython
* PyZMG - zmq bind + nice I/O event loop adapted from Tornado

Circus Architecture
====================

TODO - Get a copy of the image from Tarek.

Recap
======

* **circusd**: daemon that watches all processes
* **circusctl**: interaction shell
* **circus-top**: Like top, but only for things Circus is managing
* **circus-httpd**: Runs the web client

TODO - get the rest of the components from Tarek

Problem
==========

Can't interact with Django workers because they are supervised by Gunicorn, which is managed by Circus.

Answer: Circus sockets - Not just sockets, but also manage processes.

* Every process managed by Circus is forked from circusd
* circusd creates & opens sockets
* child processes can accept() connection on those sockets

WSGI
======

* Chaussette: WSGI server that reuses already opened sockets
* Launched with the socket...
* TODO - catch up

Benchmarks
===========

Circus + gevent is slightly faster than Gunicorn + gevent. 
=====================================================
Python distributed programming using gevent and redis
=====================================================

by Alex Dong

* http://trunk.ly/?q

Roadmap
========

* Crawler: the unsung here
* Async 101
* Gevent: the monkey king
* Redis: data structure server
* lessons learned

How many links does google index?
=================================

* 18 million when it started
* Only 2-3 billion right now
* First project google employee worked on was the crawler

Talking about a crawler
=======================

1. Get a url from a task queu
2. DNS resolution
3. Request HTTP Header
4. Download full content
5. Store to local file store, database and index

Add in scheduling, throttling, status monitoring, scale up by flicking on more servers.

Async 101
=========

* Whats wrong with multi-thread
    
    * GIL issues
    * Yield on IO/socket, but
    * Computational expensive will block
    
* What about multi-process?

    * Memory efficiency
    * Context switch overhead

The overhead of multi-process in Python causes a lot of server load.

Another way
------------

* controller + worker model
* Cooperative multitasking
* Some unix code::

    epollfd = epoll_create();
    epoll_ctl(epollfd, EPOLL_CTL_ADD, listen_sock, &ev)
    epoll_wait(epollfd, events, MAX_EVENTS, -1)
    
gevent - Monkey King and Pool
===================================

Monkey patches python and magically makes multi-processing work.

.. sourcecode:: python

    from gevent import monkey
    monkey.patch_all() # patches the Python magically

    from gevent.pool import Pool
    worker_pool = Pool(size)
    # get domain into payload
    pool.spawn(socket.getaddrinfo, payload)
    
Question: Whats the downside?

 * Alex says that it makes debugging harder
 * Hence the lesson of making a dashboard!

Redis - Data Structure Server
=============================

* High performance 15,000 req/sec

    * Lock free, single process
    * master/save ready
    
* Data Structures

    * FIFO queue: Lists - LPOP, RPUSH
    * Working hashtable - HSET, HDEL
    
.. note:: lots more I didn't get in! 

Lessons Learned - Dashboard
==============================

* Turning point: Most important code we've written
* 25% code for status update and monitoring
* What's causing the piling up?

    * Someone abusing the system?
    * DNS is down?
    * ISP's bandwidth?
    * Large file download?
    * Scheduler re-submit tasks?

Lesson Learned - Fine balance
==============================

* Conflict between frontend an backend
* Capacity planning

Example: *If the worker takes too long to return control you can block your system*

Lessons Learned - Use Profiler
==============================

* Structure the code to make it possible to run all steps in one non-gevent enabled process
* Carefully profile to make sure `socket.recv` becomes the main bottleneck
* Rule of thumb `load average` < 1 to saturate 10M Bandwith

Question: Where they using regex to parse HTML?
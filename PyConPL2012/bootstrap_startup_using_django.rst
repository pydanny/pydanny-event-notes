=============================================
How to bootstrap a startup using Django
=============================================

* by Jannis Leidal

    * https://twitter.com/jezdez
    * https://github.com/jezdez
    * Django core dev
    * DSF and PSF member
    * Co-maintainer of pip/virtualenv
    * works on PyPI
    * Lead engineer at http://gidsy.com

Talk Description
================

Based on the experiences building Gidsy.com this talk will give you valuable insights as to how your infrastructure will evolve and how to set up the basic components (load balancer, web servers, DB, caching, celery, CDN, …) of your site.


What is Gidsy?
================

Gidsy is a place where anyone can explore, book and offer things to do.

Why did they choose Django?
===========================

* Big community
* Network
* Language
* Many problems already solved
* The Admin

Why Django is a good choice?
==============================

* Proven technology by similar use cases
* Stable APIs in a well-defined release process
* Good documentation with focus on prose
* Huge community of 3rd party components

Implementing search
=====================

**Haystack**:  http://www.haystacksearch.org/

* Needed customizable search abstraction
* Indexing, filtering, faceting, "More like this"
* Spatial search and sorting

Implementing API
=================

**Tastypie**: http://tastypieapi.org/

* Highly customizable Web API library
* Hooks for auth, throttling, caching, etc
* Backbone.js compatible

Task Queues
============

**Celery**: http://celeryproject.org/

If you have a user triggered process that will take a long time, use an asynchronous task queue to manage the task

* Async code execution
* Generate thumbnails, search index updates, caching, etc
* Collect stats without blocking

Caching
========

**Memcached**

* Periodic cache refreshing for high traffic sites
* Fragment caching with dates and cache version
* Cache warming during deployment

Questions
============

* Do they use a specific Catching library or the Django API?

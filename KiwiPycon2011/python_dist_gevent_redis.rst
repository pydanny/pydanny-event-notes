=====================================================
Python distributed programming using gevent and redis
=====================================================

by Alex Dong

Roadmap
========

* Crawler the unsung here
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
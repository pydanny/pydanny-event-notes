=======
Caching
=======

The difference between a site that scales well versus what doesn't comes down to caching.

 * tomoayko/writings/things-caches-do
 
Cache backends to use
=====================

 * memchached is the way to go
 * tokyocabinet is an alternative to memcached. But Jacob seems more familiar memcached
 * for testing you can explore
 
   * filesystem
   * database
   * local memory
   
Cache setup
===========

settings.py::

    CACHE_BACKEND = 'MEMCACHED://10.0.0.100:11211/'
    CACHE_BACKEND = 'file:///tmp/cache'    

Per Site Cache
==============

 * Django has a built-in cache. 
 
   * This is good for read-heavy sites.
   * Not good for write-heavy sites
   * All or none solution
   

Code::
   
    MIDDLEWARE_CLASSES = (
        'django....UpdateCacheMiddleware',
        ...
        'django....FetchFromCacheMiddleware',
    )

    CACHE_MIDDLEWARE_SECONDS = 600
    CACHE_MIDDLEWARE_KEY_PREFIX = 'mysite'
    CACHE_MIDDLEWARE_ANONYMOUS_ONLY = True
    
Details:

 * Only GET requests are cached
 * URL captures are added to the cache key
 * The cache middleware and per-view share the same logic
 * Cache keys are opaque, so cache invalidation is difficult
 
Template fragment caching
=========================

sample::

    {% load cache %}
    {% cache 600 author_info author.id %}
        {{ author.render_something_expensive }}
    {% endcache %}
    
Low-level cache API
===================

various Cache methods::

    * set(key, value, timeout)
    * get(key, default)
    * add(key, value, timeout)
    * get_many([key1, key2, ...])
    * delete(key)
    * incr(key, amt=1)
    * decr(key, amt=1)
    
Documentation
=============

 * http://djangobook.com/en/2.0/chapter15/
 * http://jacobian/r/django-cache
 
Cache decorators
================

Ack, focusing on work issues so not taking notes.

Conditional view processes
==========================

Doesn't save performance but does save bandwidth


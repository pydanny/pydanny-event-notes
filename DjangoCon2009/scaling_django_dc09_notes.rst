===============================
Scaling Django web apps
===============================

By Mike Malone
~~~~~~~~~~~~~~~

 * Common bottlenecks
 * Django gave stuff for free
 * Scaling is not speed or performance
 * Not affected by performance
 * No silver bullet
 
A Scalable Application
~~~~~~~~~~~~~~~~~~~~~~

 * Writing to local disk will kill performance
 * A scalable system doesn't need to change when the size of the problem changes

Caching
~~~~~~~

 * Per site cache (except for forms)
 * per view cache 
 * heavily personalized sites don't work this way
 
Django has a nice low-level Cache API
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 * from django.core.cache import cache
 * Use signals.post_save so you can invalidate caches
 * They would do a hack by using cache.set to None for certain cases
 
Monkey patching the cache backend lets you tie the django.cache system to memcache

Upping your appserver
~~~~~~~~~~~~~~~~~~~~~~~

 * Load balancing
 
Need to see the slides
~~~~~~~~~~~~~~~~~~~~~~~

 * Tons of details dumped really fast
 * Lots of good sys admin information
 
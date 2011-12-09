===================================
Cache rules everything around me
===================================

By Jacob Burch

 * Engineer at Revsys with me
 * Former CTO of Mahalo

By Noah Silas

 * Engineer at Causes.com
 * Former head architect of Mahalo
 
Intro to caching
====================

 * Caching is post-process data
 * Stored in a key/value store
 * Usually Done to:
 
    * Speed up your app
    * Lesson load on third party apps
    
Big Picture
====================

Jacob's rule of architecture
------------------------------

 * No rules only principals
 * Start with assumptions/advice
 * Benchmark/inspect before you break principals
 
Ask some questions
------------------

 * Do you really need caching? Caching adds...
 
    * complexity
    * additional point of failure
    
 * Modern database are stupidly optimized
 
    * May be all you need!
    
*There are only two things in Computer Science, cache invalidation and naming things* - Phil Karlton

Relying on your cache always being up
------------------------------------------

 * Rely on a single canonical data source
 * This data source IS NOT YOUR CACHE
 

Common Cache Patterns
---------------------- 

 * Rollup values often called like settings
 * Only do it for common data calls
 * What's easy:
 
    * cache invalidation is relatively easy
    
 * What's hard
 
    * Known when to invalidate
    
Thundering herd problem
------------------------

 * If everything in your cache tries to reload at once because you had a service outage
 * Huge load on your system and third party apps
 
    * You may get throttled by other systems

The New Hotness Pattern
------------------------------

 * Cache Forever, Invalidate, explicitly
 
    * Keep the cache forever
    * Invalidate only when the data changes
    * Add the data back right then and only for that bit
    
 * Use celery or deferred to handle long processes
 
Key-holding
-------------

 * How about storing cache keys in a file?
 
How to avoid Cache Invalidation Hell
========================================

Yay!

What's in the box
-----------------

 * django.core.cache
 
    * simple setup
    * Multi Cache Support
    
 * django.core.cache.backends (best way)
 
    * memcached.MemcachedCache (works with PyPy)
    * memcached.PyLibMCCache (faster but on C)
    * 
    
 * View decorators are interesting because they cache HTML

    * But you don't know cache key names so that makes invalidation hard
    
 * `{% load cache %}` DON'T USE THIS!!!
 * django.core.cache
 
    * settings.CACHES[alias]['VERSION']
    * settings.CACHES[alias]['KEY_PREFIX']
    * settings.CACHES[alias]['KEY_FUNCTION']

.. sourcecode:: python

    def make_key(key, prefix, version):
        return ':'.join([prefix, str(version), smart_str(key)])
        
Good cache keys
---------------

 * Make them unique
 * Use separators that don't appear in your values
 * Don't ever write the same format string once

Key files!
------------

 * Don't define the same key format string in more than one place
 * Put all the app key names into one file

.. note:: What I tend to do is as follows

.. sourcecode:: python

    # in core/cachekeys.py I store all my cache keys in functions
    def profiles_profile(user):
        return "profiles:profile:{pk}".format(pk=user.pk)
        
    # Then I refer to the key thus in a models file
    from django.contrib.auth.models import User
    
    from core import cachekeys
    
    class MyModel(models.Model):    
    
        user = models.ForeignKey(user)
    
        def get_profile(self):
            key = cachekeys.profiles_profile(self.user)
            profile = cache.get(key)
            if profile is not None:
                return profile
            profile = self.user.get_profile()
            cache.set(key, profile)
            return profile
            
        def save(self, *args, **args):
            profile = self.user.get_profile()
            cache.set(key, profile)        
            # TODO add superclass call here
            
    
    
Cache related code stuff
--------------------------

 * try MyModel.cache as a manager

    * `User.cache.get_top10_users.all()`
    * This is really djangsta!
    
 * invalidation: 
 
    * try a post_save signal to separate concerns. Hrm...
    * Using signals can make cache invalidation hard
    * They have to do model.save() magic to make their system
    * QUESTIONS: Aren't they losing that separation? Why not a save() override instead of signals? Wouldn't it be less engineering to just put it all in the save()? 
    
        * The answer is that they are breaking principals
        * Not a clear answer on what they are getting out of post_save stuff then
    
.. sourcecode:: python

    # TODO - Get their OriginalStateModel code
    
Third Party tools
==================

 * TODO - get this list!
 
Last minute Advice
===================

 * Don't let your cache servers be accessible
 * consistent hashing is a neat trick -- use it!
 
DoesNotExist Deserves Cache love
--------------------------------

sfsf
    

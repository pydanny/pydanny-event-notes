==================================
Using Django in Non-Standard Ways
==================================

by Eric Florenzano

 * Categories

  * Choosing alternatives to what Django offers
 
  * Using bits of Django in other contexts

The main thing
---------------

Its not as hard as you think its going to be.

Choosing alternatives
----------------------

 * Use Jinja2 with Django.
 
  * More performant
  
  * Some people like it more
  
Check out his slides for how it was done. In Django 1.2 you can just write a custom template loader.

What about my apps?
~~~~~~~~~~~~~~~~~~~

 * Sometimes you just have to rewrite your template code.
 
Not using django.contrib.auth
------------------------------

 * Sometimes it will be more difficult than not using it
 * When using it will make your code less straightforward than not using it
 * ie a facebook app
 
How to do it:

 1. Create a tiny app with one model whose PK is the Facebook User ID
 2. Wrote one decorator function redirect to an authorization page if not auth'd
 3. Convert a few apps to use the tiny app's key instead of django.contrib.auth.model.User
 
Not using the ORM?
--------------------

If against a database, why not write a pluggable Database backend? Cause writing that is non-trivial.

*Too much detail to notate but check this out below. Its a way to use settings without a settings file!*

Gem::

    from django.conf import settings
    settings.configure(USE_I18N=False)
    
Using the ORM in stand-alone mode
---------------------------------

#. Make sure the app with models is on your python path
#. Call settings.configure with your DB info
#. Optionally copy manage.py to your project
#. import your models and use them

WSGI Middleware
----------------

 * Start looking at repoze
 
  * repoze.bitbt - Scales images
  
  * repoze.squeeze - Merges JS/CSS based off statistical analysis
  
  * repoze.profile - Aggregates Python profiling data across all requests, and provides an HTML for viewing the data
  
Other
--------

 * Yardbird - IRC using Django's URL mapping to match messages and views into handling the callbacks
 * Djng - Django based microframeworks
 * Jng - Single file CMS
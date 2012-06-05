===================================
Using CSS preprocessors effectively
===================================

by Jonas Wagner

* Known for doing crazy and creative stuff
* Porting Physic engines to JavaScript via Python
* Works as Software Engineer at local.ch
* 3.1 million unique clients


Don't make a mess
==================

* Most programming languages encourage good code pattern
* CSS is not one of those languages

Issues with CSS
===============

* No Variables
* No hierarchy
* Prefixes
* Sprites
* Lack of abstraction

Solution: CSS Preprocessors
==============================

Choosing a Preprocessor

SASS
----

* Official implementation is in Ruby
* Two dialects scss and sass
* Sassy CSS
* Syntactically Awesome Stylesheets
* PySCSS is an implementaton of SCSS in Python
* Compass is 

LESS
----

* Originally written in Ruby
* Now implemented using JavaScript in Node.js
* Can be compiled on the client and using Node.js
* Twitter bootstrap uses LESS

Which one?
----------

* Features virtually equivalent
* Both are a superset of CSS
* He recommends SCSS

    * More explicit syntax
    * Compass offers lots of goodies
    * Decent Python implementation
    
Common Features
===============

* Variables
* math and functions
* nesting
* avoiding CSS hacks
* More elegant comment system
* Mixins
* Prefixes

Doing it with Django
=====================

.. parsed-literal::

    pip install webassets cssmin
    
.. code-block:: python

    STATICFILES_FINDERS = (
        ...
        'django_assets.finders.AssetsFinder',
    )

    INSTALLED_APPS = (
        ...,
        'django_assets',
    )

in assets.py:

.. code-block:: python

    from django_assets import Bundle, register
    js = Bundle('common/jquery.js', 'site/base.js', 'site/widgets.js',
                filters='jsmin', output='gen/packed.js')
    register('js_all', js)

.. code-block:: django

    {% load assets %}
    {% assets "js_all" %}
        <script type="text/javascript" src="{{ ASSET_URL }}"></script>
    {% endassets %}

Tools
======

* Good editor support for Preprocessors
* Graphical tools like LiveReload and Compass.app
* FireSASS

Warning
========

* Increased complexity
* Might not work with IE
* Makes debugging harder
* Potential for bloat

Conclusion
============

* Preprocessors solve common problems
* Allow us to focus on writing clear and meaningful CSS
* Try it on at least one project
* Plain old CSS feels very silly
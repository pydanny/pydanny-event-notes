==================================================================
Meta-matters: Using decorators for better Python programming
==================================================================

by Dr. Graeme Cross 

.. note:: I have a **lot of trouble writing decorators and I'm here to correct it!**

The preamble
============

* An intro to writing reading/writing decorators
* Python 2.6/2.7 only
* Assumes you have a basic understanding of Python, writing functions and writing classes
* Slides and content at https://bitbucket.org/gjcross/talks


.. warning:: Designed for clarity and not production code!

What is a decorator?
=====================

* A function or class that modifies or extends another function or method
* Nothing fancy and nothing new
* aspect oriented programming 
* Just syntactical sugar

.. sourcecode:: python

    @cache
    def factorize(n):
        factors = []
        # calculate factors of n
        # takes lots of time for large n
        return factors

Why use decorators?
====================

* Robust design

    * separation of concerns
        
        * example: you can work the function and not the caching
    
    * Can easily turn behavior on/off
    
* Improved readability

    * Less baggage in code (Cache code is outside the function)
    * less lines of boilerplate
    * less code duplication
    * simplifies 
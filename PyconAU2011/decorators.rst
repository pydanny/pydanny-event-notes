==================================================================
Meta-matters: Using decorators for better Python programming
==================================================================

by Dr. Graeme Cross 

.. note:: I have a **lot of trouble writing decorators and I'm here to correct it!**

Question: How do we write decorators so that Sphinx/Docutils can handle decorated stuff?

The preamble
============

* An intro to writing reading/writing decorators
* Python 2.6/2.7 only
* Assumes you have a basic understanding of Python, writing functions and writing classes
* Slides and content at https://bitbucket.org/gjcross/talks


.. warning:: Code examples are designed for clarity and not for production code!

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
    * simplifies code maintenance
    
* Widely used in Python libraries & frameworks

Why wouldn't use Python?
=========================

* Not built into Python 2.3 or earlier
* Can slow your code down (nested functions can sink your performance)
* Can hamper debugging when a decorator is written badly
* Documentation doesn't seem to work so well

Decorator Syntax
==================

 * stackable
 * prefixed with '@'
 * can have arguments
 * same for functions, methods and classes

.. sourcecode:: python

    @assert_inputs
    @log_event
    @validate_item
    def itemable(x, y, z):
        a = x * y * z
        return a

Typical uses
============

preconditions and post-conditions
----------------------------------

    * Assert types
    * check returned values
    * authentication
    * authorization

Awesome ideas I need to use ASAP!
----------------------------------------

    * debugging
    * logging
    * locking of resources (threading, io, database)
    
        * maybe deprecated by `with` statement?
        
    * threads
    * hardware

Classic decorators
===================

Properties! (A favorite of mine!)

.. sourcecode:: python

    class Love(object):
    
        @property
        def fiance(self):
            return 'Audrey Roy'

Let's write a decorator!
========================

* See PEP 318
* Because functions are objects you can pass them around with state and all that...

.. sourcecode:: python

    # remember functions are just objects, right?
    import math
    
    def trig_power(trig_func):
        print "Storing function=", trig_func
        
        def power(deg, n):
            return math.pow(trig_func(deg), n)
        return power
        
    if __name__ == "__main__":
        sine_power = trig_power(math.sin)
        tan_power = trig_power(math.tan)
        
Another example:

.. sourcecode:: python

    def report_entry(func):
        print 'Just entered a %s function' % func
        return func
        
    @report_entry
    def add2(n):
        ''' I add two '''
        return n + 2
        
    if __name__ == "__main__":
        print add2(5)
        help(add2)
        
The problem with docstrings and wrappers:

.. sourcecode:: python

    def report_entry(func):
        print 'Just entered a %s function' % func
        
        def wrapper(*args):
            ''' our internal wrapper thingee '''
            print 'This will be our docs issue'
            return func(*args)
            
        return wrapper
        
    @report_entry
    def add2(n):
        ''' I add two '''
        return n + 2
        
    if __name__ == "__main__":
        print add2(5)
        help(add2)
        
A better version of our decorator
===================================

from functools import wraps

.. sourcecode:: python

    def report_entry(func):
        print 'Just entered a %s function' % func
        
        @wraps(func)
        def wrapper(*args):
            ''' our internal wrapper thingee '''
            print 'This will be our docs issues'
            return func(*args)  
        return wrapper
        
    @report_entry
    def add2(n):
        ''' I add two '''
        return n + 2
        
    if __name__ == "__main__":
        print add2(5)
        help(add2)

Best practices for using decorators
====================================

* Document them well
* If you stack them, notate where stacking them can be a proble,
* Use the `functools.wraps` decorator for internal functions
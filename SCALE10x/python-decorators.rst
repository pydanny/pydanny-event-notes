=====================================================================
It's all good- Decorating Python like Martha Stewart
=====================================================================


* by Matt Harrison
* http://twitter.com/_mharrison_
* Works for http://fusion.io
* http://hairysun.com/books/decorators/

    * His talk is under creative commons
    
Impetus
=========

You can get by in Python with basic constructs but...

* you might get bored
* be confused by other's code
* want more power

Function Review
================


A function is an instance ot type function

.. sourcecode:: python

    >>> def spam():
    ...     "A function"
    ...     print 'eggs'
    >>> spam
    <function 0x2342342>
    >>> callable(spam)
    True
    >>> spam()
    'eggs'
    
Functions have attributes

.. sourcecode:: python

    >>> spam.func_name
    'spam'
    >>> spam.__docstring__
    "A function"
    
A function knows about itself

.. sourcecode:: python
    
    >>> def foo2():
    ...     print "NAME", foo2.func_name
    
A function can have attributes assigned:

.. sourcecode:: python

    >>> def foo2():
    ...     print "STUFF", foo2.stuff
    >>> foo3.stuff = "Data"
    >>> foo3()
    Data

Function Definition
======================

.. sourcecode:: python    

    def func_name(arg1, arg2=value, *args, **kwargs):
        """ docstring """
        # implementation
    
Function Gotcha
===============

When a function is created, the named/default parameters are defined when the function is created

.. sourcecode:: python    

    def named_param(a, foo=[]):
        if not poo:
            foo.append(a)
            
    print named_param.func_defaults
    ([])
    
    named_param(1)
    print named_param.func_defaults
    ([1, ])
    
Lists and dicts are mutable. When you modify them you don't create a new list (or dict). Strings and ints are immutable

Parameters are evaluated when the def they belong to is imported

Don't default to mutable types.

.. sourcecode:: python    

    def named_param(a, foo=None):
        foo = foo or []
        if not foo:
            foo.append(a)
            
*args and **kwargs
====================

Looksee:

* *args is a tuple of parameter values.
* **kwargs is a dictionary of key/values

.. sourcecode:: python

    def param_func(a, b=2, c=5):
        print [x for x in [a, b, c]]

The '*' before args flattens the tuple of parameters values.

.. sourcecode:: python

    def param_func(a, *args):
        print [x for x in [args]]
        # TODO  check I got this right

    def kwargs_func(a, **kwargs):
        print [x for x in [kwargs]]
        # TODO  check I got this right

    def param_func(a, b='b', *args, **kwargs):
        print [x for x in [a, b, args, kwargs]]
        
Closures
==============

* PEP 227 and came out in Python 2.1
* Don't be afraid of them
* In Python a function can return a new function. The inner function a closuse and any variable it accesses that are defined outside of that function are free variables.

.. sourcecode:: python

    def add_x(x):
        def adder(num):
            # we have read acces to x
            return x + num # x is a free variable here
        return adder
        
    sadd_5 = add_x(5)
    add_5 # doctest: + ELLIPSESS
    <function add at 0x12324ewe>
    print add_5(10)
    15
    
Nested functions only have write access to global and local scope.

.. sourcecode:: python

    x = 3
    def outer():
        x = 4 # now local
        y = 2
        def inner():
            global x
            x = 5 # 
        print x
        inner() # only changes the local inside the function
        print x
    print outer()
    4
    4
    print x # since global the global value
    5
    
Python 3.x has a non-local keyword that replaces the global in Python 2.x

Decorators
===========

* PEPS 318, 3129, implemented in Python 2.4
* allow you to

    * modify arguments
    * modify function
    * modify results

.. sourcecode:: python

    # count how many times a function is called
    call_count = 0
    def count(func):
        def wrapper(*args, **kwargs):
            global call_count
            call_count += 1
            return func(*args, **kwargs)
        return wrapper
    
    def hello():
        print 'invoked hello'
        
.. sourcecode:: python        

    >>> hello = count(hello) # invoking count with the argument being the hello object
    >>> hello()
    >>> print call_count
    >>> 1
    >>> hello()
    >>> print call_count
    >>> 2
    
.. sourcecode:: python            
    
    # Decorator Shortcut
    @count
    def hello():
        return 'hello'
        
Better decorator:

.. sourcecode:: python 

    def count2(func):
        # TODO - show this one out
        
Decorator Template
==================

.. sourcecode:: python 

    def decorator(function_to_decorate):
        def wrapper(*args, **kwargs):
            # do something before invoation
            result = func_to_decorate(*args, **kwargs)
            
            # do something after
            return result
        # update wrapper.__doc__ and .func_name
        # or functools.wraps
        return wrapper
        
.. sourcecode:: python 

    # class as a decorator
    class decorator_class(object):
        def __init__(self, function):
            self.function = function
        def __call__(self, *arg, **kwargs):
            result  = self.function(*arg, **kwargs):
            # do stuff to result
            return result
            
    @decorator_class
    def hello():
        return 'hello'
        
.. note:: Anything that is callable can be used to create a decorator

.. sourcecode:: python 

    # using a class instance as a decorator
    # instead of using __call__ use __init__ and then instantiate the class before using it.
    deco = Decorator()
    
    @deco
    def hello():
        return 'hello'    
        
    # You can modify deco later! This is UBER powerful!
    
.. note:: Not the same as "Class Decorators". See PEP 3129

Paramterized decorators
========================

* need 2 closures

.. sourcecode:: python 

    def limit(length):
        def decorator(function)
            def wrapper(*args, **kwargs):
                result = function(*args, **kwargs)
                result = result[:length]
            return wrapper
        return decorator
        
    @limit(5) #notice parens
    def echo(foo): 
        return foo
    
    # usage
    echo('123456') 
    '12345'
    
    #syntactical sugar for
    echo = limit(5)echo
    
Warning: Function attributes get mangled in decorators
========================================================

* I've run into this - when you wrap a function a decorator the attributes get lost
* Docstring kills me
* Do this:

.. sourcecode:: python 

    def limit(length):
        def decorator(function)
            def wrapper(*args, **kwargs):
                result = function(*args, **kwargs)
                result = result[:length]
            return wrapper
            wrapper.__docstring__ = function.__docstring__
        return decorator

You can also use functools to deal with this issue, but it's not as clear a read

.. sourcecode:: python 

    import functools
    def limit(length):
        def decorator(function)
            @functools.wraps(function)
            def wrapper(*args, **kwargs):
                result = function(*args, **kwargs)
                result = result[:length]
            return wrapper
            wrapper.__docstring__ = function.__docstring__
        return decorator

Uses for decorators
====================

* caching

    * I wrote a cache decorator that uses Raymond Hettinger's LRU cache code.

* monkey patching stfio
* jsonify
* logging time in function call
* change cwd
* timeout a function call

What if I want to tweak decorator paramers at runtime?
============================================================

What if I made a mistake in a param and want to change values?

* Use class instance decorator
* Tweak wrapper attributes
* Use context manager
* or...

    * Since a decorator is just a class you can invoke it at runtime. Like this:
    
.. sourcecode:: python 

    # TODO get example
    result = limit(4)(echo)
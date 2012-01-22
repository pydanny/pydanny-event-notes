=====================================================================
It's all good- Decorating Python like Martha Stewart
=====================================================================

.. note:: Had to speak up because people were beginning to ask off-topic questions. After that the questions were dead on. Note to talk attendees: If the speaker lets you ask questions during the talk, please stay on topic.

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
    hello = count(hello)
    hello()
    print call_count
    1
    hello()
    print call_count
    2
    
    
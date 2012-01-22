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
================================
Functional Programming in Python
================================

* by Malcolm Tredinnick
* malcolmt
* Started in Python in 1.4

Intro
=======

* Python is more than just OO, it's also functional
* Almost every language we use is imperative
* Python can be functional

The cheatsheet for this talk
====================================

* **map()**
* **filter()**
* **functools** module
* **itertools** module
* list comprehensions
* generators

Functional programming is....
==============================

* ... difficult to define precisely
* Good! (most worthwhile systems are)

Maybe this?
-------------

* transform data structures, don't manipulate state

Most useful?
--------------

* concentrate on function return values, not side-effects

Python Functions
==================

* Functions are first class objects
* You can pass them around as arguments to other functions
* You can construct them dynamically

.. code-block:: python

    def my_function():
        print "hello"
        
    def show_string(func, arg):
        print func() + arg
        
    >>> show_string(my_function, " Goodbye!")
    hello Goodbye!
    
Useful language features
===========================

* **lambda** expressions
* **functools** module

    * TODO: check out partial() capability in **functools**

* **itertools** module

Pull out the even numbers
==========================

.. code-block:: python

    # The old way
    def evens(seq):
        results = []
        for item in seq:
            if item % 2 == 0:
                results.append(item)
        return results
        
    # List comprehension way
    def evens(seq):
        results = [x for x in seq if x % 2 == 0]
        return results
        
    # pull out the even numbers
    def is_even(value):
        return value % 2 == 0
        
    def evens(seq):
        return filter(is_even, seq)
    
    # using partials
    from functools import partial
    
    def is_even(value):
        return value % 2 == 0
        
    evens = partial( filter, is_even)
    
    >>> evens([1, 2, 3, 4, 5])
    [2, 4]
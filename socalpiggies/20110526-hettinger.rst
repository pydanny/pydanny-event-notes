
================================
Fun with Python's newer tools
================================

by Raymond Hettinger

You should be on Python 2.7!
============================

* To be supported for 5-10 years
* Earlier you convert the better


collections.Counter
===================

Tool for making rapid tallies or counts

* Modeled after:

    * Multisets in C++
    * Bags in smalltalk and Objective C
    
Very flexible, unrestricted implementation as a directory

You can put anything in it:

    * Count with positive and negative numbers
    * Count with decimals, floats, or fractions
    * it is just a dictionary
    
Simple design as a dict subclass!
---------------------------------

With __missing__() that returns zero::

    c[x] += 1 # easy to tally
    
Has __delitem__() to match __missing__()::

    del c[x] # easy to delete

Convienance methods
--------------------

    * most_common(n)
        
        * returns sorted list of the n highest counts
        * reduces the code to a simple one-liner
        * implemented using either sorted() or heapq.nlargest()
        
    * elements
        
        * lists all the contents individually
        * if an element has a count of three, it is emitted three times
        * Differs from __iter__ which returns pairs
        * Done this way because otherwise you change the **dict** API.
        
    * Multiset use case
    
        * With multisets, the counts are always positive
        * Math operations with omit zero or negative counts from the result
        * Operations are: + - & |
        * The subtraction operation is said to be saturating
        * When the counts are all one, works just like regular sets
        
collections.namedtuple()
========================

Works just like a regular tuple and lets you assign names to each field.

    * Makes the code self-documenting
    * Makes the printed __repr__ intelligible
    * Let's you change tuple order without affecting client code
    * No extra memory cost over tuple

One of the best single best changes you can make to existing code.

Doing an enum in python (not needed but its kind of cool)::

    Color = namedtuple('Color', 'red orange yellow')._make(range(3))
    
Caching
========

Simple unbounded caches can grow without bound.

How to do it::

    from functools import lru_cache
    
    @lru_cache(maxsize=100)
    def big_computation(*args):
        ...

Fibonacci example::

    @lru_cache()
    def fibonacci(n):
        if n <= 1:
            return n
        return fibonacci(n-1) + fibonacci(n-2)
    
    print(fibonacci(5))

Grotesque Hacks
=================

Fun things to do with Python

Not so bad
-----------

The iter() function has a two argument form that takes a sentinal value::

    for block in iter(partial(f.read,20), "")
        ...
        
Awesome way to stop a loop!

Dicts
-----

Use DefaultDict for 2-D sparse arrays::

    d = defaultdict(dict)
    d['Canada']['Quebec'] = 1
    
Getting grotesque
-----------------

Make dict sparse to speed up a dictionary::
    
    d.update(dict(d)) # doubles space in hash table
    
Wrap it up in a function::

    def sparser(d):
        return d.update(dict(d)) # doubles space in hash table
    
Turn-off thread-switching (cheap locking)::

    ci = getcheckinterval(0)
    sys.setcheckinterval(0) # switching off
    value = max(tasklist)
    tasklist.remove(value)
    sys.setcheckinterval(ci) # switching on

Atomic actions (no locks required)::

    v = d.pop(key) # find and remove in one-step
    d.setdefault(key, []).append(v) # one-step init

Speed-up builtin access::

    from __builtin__ import *
    
Slow constant-function::

    >>> def make_constant_function(x):
    ...     return lambda x=x: x
    >>> f = make_constant_function(3)
    >>> f()
    3
    
Fast constant functions::

    >>> def make_constant_function(x):
    ...     return itertools.repeat(x).next
==========================
Data Structures in Python
==========================

by Alex Gaynor

Python is awesome because it implements basic data structures as described by Knuth. 

Paraphrase: *The Python core has read Knuth so we don't have to!*

Alex Commandments

#. Use types idiomatically
#. Sometimes you don't get a choice
#. Be efficient, when it doesn't cost you anything
#. sometimes you habe more than one concern to deal with. The standard lib can help!
#. Don't do more than you have to: collections.abc are there to help.


Builtins
==========

* list vs tuple
* list vs set
* set vs frozenset

list vs tuple
--------------

"I only use tuples if using a namedtuple would be equally appropriate"

Not a performance or mutability issue, but use them idiomatically

sets vs lists
-------------

* lists have an order, sets don't
* sets must be hashable
* sets let you check for uniqueness super-fast

sets vs frozenset
------------------

blah blah

The stdlib
===========

collections.OrderedDict
-----------------------

* new in 2.7
* For when you have a dict that needs an order
* Syntax::

    OrderedDict([
        ("name":Field),
        ("type":Field),
        ("state": Field),
    ])
    
collections.deque
-----------------

* Fact: list.pop(0) and list.insert(0) are slow
* Good for in memory logs and such

Other
------------

* Array: Good for a bunch of types of the same sort
* heapq: Look into it.

Do It Yourself
================

When you have to do it yourself use collections.abc!

* abstract base classes for extending collections
* Because you **don't subclass dict ever!!!!**

    * Subclassing Python's builtin containers tends not to behave as we want
    * Subclassing the ABCs does

* OrderedSet example: http://code.activestate.com/recipes/576694/

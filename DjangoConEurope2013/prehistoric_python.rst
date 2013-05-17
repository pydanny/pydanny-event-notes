========================================================
Prehistorical Python: Patterns past their prime
========================================================

by Lennart Regebro

    * Freelancer
    * Django, Pyramid, and Zope guy
    * One of the tech reviews of `Two Scoops of Django`_!
    * Author of `Porting Python Python 3`_
    
        * worth it if you are upgrading from Python 2 to 3!
    

.. _`Porting Python Python 3`: https://gumroad.com/l/python3
.. _`Two Scoops of Django`: https://2scoops.org

There are many idioms and patterns that used to be a best practice but isn't anymore, thanks to changes in Python. Despite that they often show up even in new code, and some of these patterns are even explained to be Good Ideas at stackoverflow and similar. 

This talk will bring out the most common of these patterns so you know what they are, and why you should avoid them.


Defaultdict
==============

.. code-block:: python

    # python 2.5
    from collections import defaultdict
    data = defaultdict()
    data[key] = value
    
    # Python 2.5-
    # Exists still in Django 1.5.1
    # django/db/models/sql/query.py
    if key in data:
        data[key].add(value)
    else:
        data[key] = set([value])
        

Sets
======

* Unique values
* Unordered
* Fast lookup
* Python built-in in 2.4

Sets before sets
-----------------

.. code-block:: python

    d = {}
    for each in list_of_things:
        d[each] = None
        
    list_of_things = d.keys()
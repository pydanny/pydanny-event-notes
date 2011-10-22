=======================================
2011/10/22 Know Your Time Complexities
=======================================

* by Ryan J. O'Neil
* rzoz on #pylaides

Whole bunch of data
=====================

Remove duplicates from a large system and remove dupes

.. sourcecode:: python

    import random
    
    choices = range(100000)
    x = [random.choice(choices) for i in xrange(1000000)]
    
    
The Bad Way
===========

.. sourcecode:: python

    order = []
    for i in x:
        if i not in order:
            order.append(i)

The Good Way
============

.. sourcecode:: python

    order = []
    seen = set()
    for i in x:
        if i not in seen:
            seen.add(i)
            order.append(i)
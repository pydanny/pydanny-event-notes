==========================================
Python is Only Slow If You Use it Wrong
==========================================

* by Avery Pennarun
* Google employee

    * But this talk has nothing to do with them
    * If you apply to google and say his name he get's money. :)

* Trying to talk about bitter


Stuff he's done
=================

* bup: Python software doing massive things for real problems

    * http://github.com/apenwarr/bup

* sshuttle: VPN software tht handles 802..11 g/n speeds in python

    * http://github.com/apenwarr/sshuttle

Easiest way to do Python wrong
================================

tight inner loops
---------------------------------

.. sourcecode:: python


    chars = open.file('file').read()
    for char in chars:
        ...
        # slow
        
* Don't do this
* Apparently for dynamically typed languages, this is a very, very slow operation
        
Speeding things up
------------------

* Use regexes and c modules
* No such thing as 100% pure python
* forget about SWIG

    * writing C modules is easy and integrating them easy too 
    * SWIG is a code generator for C++
    
* python + C is so far the winning combination
* C is simple; Python is simple; PyPy is hard

    * The concept behind PyPy is really hard
    * Python and C are relatively straightforward compared to the concepts of PyPy
        
.. note:: I want to learn how to write C and then add it to my Python work.

Other way to do things wrong
================================

* Computation threads

    * Worthless becauxe of GIL
    
* Threads are okay for I/O
* fork() works great for both
* C modules that use threads are fine

Garbage Collection
===================

Refcounting
-----------

* Every time I use a variable I increase its reference count by one
* Every time I don't use something its reference count goes down by one
* When it hits ZERO then it goes away

Refcount... and threads: BAD COMBO
---------------------------------------

* Variable shared between threads forces a lock on the refcount
* One reason why removing the GIL is almost impossible
* There are tricks...

Python is not a garbage collected language++
--------------------------------------------


.. sourcecode:: python

    for i in xrange(1000000):
        a = '\0'*10000

* Sample code in Python
* Metric test done in **Python**, **PyPy**, **Java**, **C**, and **Go**

    * **Java**: Running this loop takes more memory and more time than CPython!
    * **PyPy** takes about the same time as Python
    * **C** is much faster
    * **Go** is much slower
    
Java is a garbage collected language
------------------------------------------

* Three different collection strategies
* See his upcoming research paper: **Seriously Java, WTF?**
* Amusingly, the new threaded java system is slower and takes more memory
* "Ever notice complex Java programs seem to run slow and take up tons of memory?"

++Exception sometimes python is a garbage collected language
------------------------------------------------------------

* Refcount sometimes fails
* Did you know Perl never drops objects? 

    * This is why you **can** have memory leaks with it.
    * Avoiding this requires a deep understanding of Perl
    
Get the most out of Python's GC
---------------------------------

* JUST AVOID IT AT ALL COSTS
* Break circular references by hand when you are done

    * trees are a good example
    * TODO: find out what he meant somehow

* Better still: use the weakref module

Deterministic Destructors

Quiz: Does this program work on win32?
--------------------------------------------

.. sourcecode:: python

    open('file', 'w').write('hello')
    open('file', 'w').write('hello')   
    # YES!!! Cause Python doesn't do Garbage Collection. refcounting FTW!
    
With real GC you habe to manually manage reosurces:

    * files
    * database handlers
    * sockets
    * locks
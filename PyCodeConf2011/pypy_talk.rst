=========
PyPy talk
=========

by Alex Gaynor

* Student at RPI
* Core Python Dev

    * cpython
    * PyPy

* Core Django Dev
* Interned at Quora and got them on PyPY

Two things go faster than C
==============================

* neutrinos
* PyPy

Story of PyPy
================

* psyco was JIT python

    * Managing it was hard
    * hardcoded for 32 bit CPUs and we are on 64 bit
    * Any changes to core Python killed pysco
    
* Years ago created a Python interpreter inside of Python

    * 2000x slower than cpython
    * ran on restricted Python (**r-python**)
    * Wrote a great compiler: now 10x slower than cpython
    * Added better garbage collection: now 4x slower than cpython
    
* New JIT for Python

    * Writing a JIT for Python sucks
    * Writing a generator for making JITs for any language is easier
    * **Factoid**: PyPY is the only project known to actually use SVN branches!
    * Doing it this way made it faster? How? Wizard Magic?

* Now PyPY is going fast:

    * Crazy that it runs so much faster than cpython
    * Hard to believe
    * Python using a JIT generator to create a JIT library?
    * Faster than cpython
    * http://speed.pypy.org/

Why you should use PyPy
=======================

Science!
---------

* Fast and scientist friendly
* Now works with numpy!

    * Not complete
    
Tools
-----

* TODO: Toolname here

    * Finding slow spots in existing code
    * Looks at Python, byte code, assembly, et al
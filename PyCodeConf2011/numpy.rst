========================================================
Future of Python and NumPy for array-oriented computing
========================================================

* by Travis Oliphant

* NumPy
* SciPy
* Array-Oriented Computed
* Enthought is hiring!

.. note:: I took Travis' tutorial on it in 2006. I want to use this for serious number crunching. Why bridge out to another language/server if NumPy can do it for me fast and right in Python?

Python fits your brain
========================

**Thesis**: Software engineering today is more about neuroscience than computer science

* Even fits the brains of Scientists
* Engineers say things differently than scientists

.. sourcecode:: python

    # engineering solution
    from scipy.signal import lfilter, lifiltic
    from numpy import zeros

    # TODO get values here

    def fibonocci(value):
        x = zeros(N)
        y, zf = lfilter(b,a,x,zi=zi)
        
* But this is not fast enough for scientists

    * C speed
    * CPU speed
    * FASTER!!!
        
Conway's Game of Life
----------------------

* http://en.wikipedia.org/wiki/Conway%27s_Game_of_Life


APL: first array oriented language
--------------------------------------------

* 1964
* Descendants still alive: J, K, matlab
* NumPy is a descendant of J
* Crazy non-standard unicode characters
* Very compact
* Can do Conway in a single line of very dense code

Derivative Calculations
------------------------

* Complex data can be memory intensive
* Big sets break even list generators
* NumPy can do this for you

History of SciPy and NumPy
===========================

* Travis started in 1997 on Python 1.4
* Early contributors added `numeric` as a Python extension

    * Jim Hugenin (`numeric`)
    * Jim Fulton
    * Paul Dubiois

* Fortran still exists because of complex numbers. Most languages got it wrong for a long time, including C and Java.


Travis Found Python and Numeric in 1997
------------------------------------------

* Was good at MATLAB but it wasn't efficient
* Loved the expressive syntax of Python
* Loved that slicing didn't make copies
* Love the multiple data types
* Much more flexible than MATLAB
* Loved that he could read source code a year later

1999: Early SciPy emerges
------------------------------

* Wanted something more complete than numeric
* A set of libraries and stuff
* Lots of early contributors

NumPy started in 2006
-----------------------

* Wasn't happy with some of the directions of Numeric
* Got it working after 18 months and the work of 6+ dedicated people

SciPy Today
------------

* Conferences
* Collection of Tools (NumPy, et al)
* Community
* being looked at by the Financial community

What SciPy Does
=====================

SciPy
-----

* Lots of cool data shaping tools

NumPy
------

* We aren't talking about simple lists but gigantic multidimensional arrays
* Super-duper fast
* Terse but understandable notation
* See `Zen of NumPy`:

    * strided is better than scattered
    * contiguous is better than strided
    * descriptive is better than imperative
    * TODO: finish writing this out!


Call to Action: Collaboration between Python Core and the Scientific Communication
==================================================================================

**Contention:** Collaboration between Python core and scientific developers needs to be tighter

* Index array operator (matrix multiplication is not domain specific)
* Use of slice notation inside function calls
* Array overloading of **and** and **or**
* DSL blocks?

Call to Action: NumPy and PyPy
================================

* Stop chasing C, start chasing Fortran. Against an example:

    * **Python**: 202 seconds
    * **PyPy**: 4.71 seconds
    * **NumPy**: 5.56 seconds
    * **Cython**: 2.21 seconds
    * **Fortran 90**: 0.8 seconds

* Mock Fortran if you will, but it is blazing fast for some important stuff.
========================================================
Future of Python and NumPy for array-oriented computing
========================================================

* by Travis Oliphant

* NumPy
* SciPy
* Array-Oriented Computed
* Enthought is hiring!

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

SciPy Today
------------

* Conferences
* Collection of Tools
* 






Aside: Call to Action
===========================

**Contention:** Collaboration between Python core and scientific developers needs to be tighter

* Infex array operator (matrix multiplcation is not cdomain specific)
* Use of slice notation inside function calls
* Array overloading of **and** and **or**
* DSL blocks?

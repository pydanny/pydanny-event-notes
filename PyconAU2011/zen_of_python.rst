=================
Zen of Python
=================

by Richard Jones

**aka 19 Pythonic Theses**

Guido's Original Design Philosophy

* borrow ideas
* As simple as possible, no simpler
* Do one thing well
* Don't fret about performance
* Go with the flow


* Avoid platform ties, but not religiously
* Don't bother the user with details


Beautiful is better than ugly
=============================

See http://en.wikipedia.org/wiki/Euclidean_algorithm::

    function gcd(a, b)
        while b ≠ 0
           t := b
           b := a mod b
           a := t
        return
        
Wikipedia's version is not as pretty as Python:

.. sourcecode:: python

    def gcd(a,b):
        while b != 0:
            a, b = b, a % b
        return a

Explicit is better than implicit
================================

File openings are not that explicit

The `:` in Python is lovely and explicit.

.. sourcecode:: python

    class Circle(object):
        
        def __init__(self, radius):
            self.radius = radius
            
        def area(self):
            """ The 'tau' value is from outside the class """        
            return tau * self.radius
            
Simple is better than complex
=============================

* Something simple is easily knowable
* Something complex is not
* Automatic memory management means code is simpler
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
* etc


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
* That we can define getter/setters and override existing ones in Python is awesome.

Getting length of objects is simple in python:

.. sourcecode:: python

    l = [1,2,3,4,5,6,7,8]
    len(l)

Try to keep your try/except blocks a small as possible. You'll thank yourself later.

Complex is better than complicated
==================================

.. note:: I never actually think about this koan.

.. sourcecode:: python

    for line in open('document.txt'):
        print(len(line), line, end='')

    # how about opening up things
    for file in glob.glob('*.txt.gz'):
        for line in gzip.

Flat is better than nested
==============================

Inheritance flattening
----------------------

* Keep object inheritance shallow
* Multiple inheritance keeps things shallow but things get more complex

    * Richard Jones worries about this
    * I don't worry that much. Never bites me the way Java did.

Break up complex structure
------------------------------

* Keep your `if/elif/else` use as light as possible
* Smaller code == Better code
=================
Zen of Python
=================

by Richard Jones

**aka 19 Pythonic Theses**

Guido's Original Design Philosophy
====================================

Timesaving concepts
-------------------

* Borrow ideas from elsewhere whenever it makes sense.
* “Things should be as simple as possible, but no simpler.” (Einstein)
* Do one thing well (The "UNIX philosophy").
* Don’t fret too much about performance--plan to optimize later when needed.
* Don’t fight the environment and go with the flow.
* Don’t try for perfection because “good enough” is often just that.
* (Hence) it’s okay to cut corners sometimes, especially if you can do it right later.

Clarity concepts
-----------------

* The Python implementation should not be tied to a particular platform. It’s okay if some functionality is not always available, but the core should work everywhere.
* Don’t bother users with details that the machine can handle (I didn’t always follow this rule and some of the of the disastrous consequences are described in later sections).
* Support and encourage platform-independent user code, but don’t cut off access to platform capabilities or properties (This is in sharp contrast to Java.)
* A large complex system should have multiple levels of extensibility. This maximizes the opportunities for users, sophisticated or not, to help themselves.
* Errors should not be fatal. That is, user code should be able to recover from error conditions as long as the virtual machine is still functional.
* At the same time, errors should not pass silently (These last two items naturally led to the decision to use exceptions throughout the implementation.)
* A bug in the user’s Python code should not be allowed to lead to undefined behavior of the Python interpreter; a core dump is never the user’s fault.


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

Sparse is better than Dense
===========================

* Is this a style guide thing?

    * whitespace?
    * naming standards
    
* I (pydanny) think it is about spartan programming

    * http://www.codinghorror.com/blog/2008/07/spartan-programming.html
    * http://ssdl-wiki.cs.technion.ac.il/wiki/index.php/Spartan_programming

* Koans by Tim Ansell

    * 14 arguments for a method is too much
    * Don't compromise on complexity by adding more complexity
    
Readability counts.
====================
    
* Koan: Readability is the number 1 reason why organizations select Python

.. sourcecode:: javascript

    if (x == y);
    {
        // logic
    };
    
    // a day wasted

Special cases aren't special enough to break the rules
======================================================

* Everything is an object

Although practicality beats purity
==================================

Sometimes the rules need to be broken:

.. sourcecode:: python

    >>> class Two(int):
    ...     pass
    ...    
    >>> print(Two(1))
    1
    >>> Two.__str__ = lambda x: '2'
    >>> print(Two(1))
    2

A better example is circular imports.

* http://stackoverflow.com/questions/3955790/python-circular-imports-once-again-aka-whats-wrong-with-this-design#3956038

Errors should never pass silently
===================================

* Errors should not be fatal
* Don't blame the user for bugs in Python

    * Either the core devs fault
    * Or the user added in ctypes
    
Check out except Exception at the bottom!
-----------------------------------------

`logging.exception(error) captures the entire error to the logs!`
    
.. sourcecode:: python

    try:
        handle_a_client()
    except socket.error, e:
        log.warning('client went away: %s', e)
    except Exception, e:
        logging.exception(e) # This captures the whole traceback!!!

In the face of ambiguity, refuse the temptation to guess.
============================================================

.. sourcecode:: python
    
        1 + '1' 
        # blows up in Python, not in other languages
        # We like this behavior!
        
Also, remove the ambiguity and whack some parenthesis
        
There should be one - and preferably only one- obvious way to do it
===================================================================

Protocols:

 * File API
 * DB API
 * WSGI
 * etc
 
Although that way may not be obvious at first unless you're Dutch
=================================================================

* Guido can be quirky
* Community feedback keeps BDFL in check

*You try to shoot yourself in the foot, only to realize there's no need, since Guido thoughtfully shot you in the foot years ago.* - TODO: find who said that

Now is better than never
========================

* Fix the problem now
* Try it in your shell, and your tests
* *Perfection is the enemy of the good*
* Python 3 was years in the making, but much less than Perl 6.


Although never is often better than *right* now.
=================================================

Things that ain't gonna happen

 * Adding '?' to identifiers in Python
  
If the implementation is hard to explain, it's a bad idea.
============================================================

If you can't say it, don't do it

If the implementation is easy to explain, it may be a good idea.
================================================================

Just because you can explain your idea, if it has no point then it shouldn't be included.

Namespaces are one honking great idea -- let's do more of those!
================================================================

* locals > nonlocals > globals > builtins
* Me (pydanny) loves this about Python

Reference: Zen of Python
========================

.. parsed-literal::

    >>> import this
    The Zen of Python, by Tim Peters

    Beautiful is better than ugly.
    Explicit is better than implicit.
    Simple is better than complex.
    Complex is better than complicated.
    Flat is better than nested.
    Sparse is better than dense.
    Readability counts.
    Special cases aren't special enough to break the rules.
    Although practicality beats purity.
    Errors should never pass silently.
    Unless explicitly silenced.
    In the face of ambiguity, refuse the temptation to guess.
    There should be one-- and preferably only one --obvious way to do it.
    Although that way may not be obvious at first unless you're Dutch.
    Now is better than never.
    Although never is often better than *right* now.
    If the implementation is hard to explain, it's a bad idea.
    If the implementation is easy to explain, it may be a good idea.
    Namespaces are one honking great idea -- let's do more of those!
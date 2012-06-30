============
Basic Python
============

* by http://twitter.com/titopao
* Python since 2007, but since early 2000s
* Affiliated of Wikimedia Philippines, Inc
* Major equipment issues including the microphone.
* Live code writing is never a good idea. :P

About Python
=============

* Started by Guido van Rossum a.ka. Benevolent Dictator for Life
* Named after **Month Python and the Flying Circus**
* Logo of Python is the snake
* Dynamically typed

Variants of Python
==================

* CPython
* Jython
* IronPython
* PyPy
* Stackless Python

Prerequisites
=================

* Python 2.7
* editor scintilla.org/SciTE.html

Hello Python
============

.. code-block:: python

    print("Hello Pycon!")

Assigning Variables
====================

.. code-block:: python

    PI = 3.1415
    answer2life = 42
    _secret_recipe = 0
    x, y = 4, 20
    
Dynamic Typing
================

.. code-block:: python

    a = 10
    a = 'python rocks'
    a = True
    b = None
    a = b
    
Numeric Data Types
====================

.. code-block:: python

    >>> print range(5)
    [0, 1, 2, 3, 4]
    >>> a = 9
    >>>b = 2.0
    >>>c = 0x999
    
Operations
============

.. code-block:: python

    >>> 2 ** 10 
    1024
    >>> abs(-1) # absolute
    1
    >>> 5 % 2 # Modulus
    1
    >>> hex(12)
    '0xc'
    >>> oct(100)
    '0144'
    >>> pow(16, 0.6)
    5.278031643091577
    
Booleans
==========

.. code-block:: python

    >>> True
    True
    >>> true
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    NameError: name 'true' is not defined
    
.. code-block:: python

    and
    or
    is
    is not
    
String Operators
=================

.. code-block:: python
    
    >>> len('Hello')
    5
    >>> 'hello'.upper()
    HELLO
    >>> s = 'Hello PyCon'
    >>> s[:5]
    'Hello'
    
Sequences
=========

.. code-block:: python

    >>> l = [1, 2, 3, 4]
    >>> t = (1, 2, 3, 4)
    >>> l.append(5)
    >>> l 
    [1, 2, 3, 4, 5]
    
Indentation
============

* Code blocks are defined by indentation
* The standard is 4 spaces. 
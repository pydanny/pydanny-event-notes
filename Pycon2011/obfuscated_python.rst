================
Obfuscated Python
================

by Johnny Healy

Really funny!

Assignment Operators
======================

Fun things you can do:

    >>> object = str
    >>> tuple = lambda *x: x
    >>> __builtins__.object = str
    

Comparisons
===========

What?!?::

    >>> object() == object()
    False
    >>> object() == object()
    False
    >>> object() == object()
    False
    >>> help((lambda x:x*x).func_code)
    ... blah blah blah
    >>> code = type((lambda x:x*x).func_code)
    >>> code
    <type 'code'>

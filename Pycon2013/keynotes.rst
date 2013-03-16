=============
Keynotes
=============

What's makes Python awesome? (Raymond Hettiger)
===================================================

* Lives in San Jose
* http://twitter.com/raymondh
* Core contributor of PyCon since forever

    * set(), frozenset(), sorted(), reversed(), enumerate(), any(), all()
    * collections, itertools,etc
    * etc
    
* I've seen previous versions of this talk. My notes at those times:

    * http://pydanny-event-notes.readthedocs.org/en/latest/PyCodeConf2011/python_is_awesome.html
    
Specifics
------------------

* License
* Commercial distros (ActiveState/Enthought)
* Zen of Python
* Community
* Repository of Modules (PyPI)
* Killer apps (Django, Pandas, etc)
* Win32
* books 

    * *Shameless plug*: I wrote a book called Two Scoops of Django. Check it out at http://django.2scoops.org

High level qualities of Python
------------------------------------

* Ease of learning
* Rapid development cycle
* Economy of expression
* Readability and Beauty
* One way to do it
* Interactive prompt
* Batteries includes
* Protocols: WSGI, dbapi, etc

.. code-block:: python

    # search directory tree for all diplicate files
    import hashlib, os, pprint

    hashmap = {} # content signature -> list of filenames
    for path, dirs, files in os.walk('.'):
        for filename in files:
            fullname = os.path.join(path, filename)
            with open(fullname) as f:
                d = f.read()
            h = hashlib.md5(d).hexdigest()
            filelist = hashmap.setdefault(h, [])
            filelist.append(fullname)
    pprint.pprint(hashmap)

Indentation
----------------------

* This is how we write pseudo-code in or out of Python
* Contributes to the uncluttered feel of the language

List comprehensions
-------------------------

* arguably the most loved feature of the language
* How much stuff should we put on one line?
    
    * Each list comprehension should represent a single English sentence

Generators
---------------

* Easiest way to write an iterator
* Simple syntax, only adds the YIELD keyword

Generator Expressions
----------------------

* Same syntax as list comprehensions but with parenthesis instead of brackets
* Acts as a generator
* reduces memory footprints exponentially.

.. note:: Giant embarrassing oops by pydanny: At PyCon Philippines 2012 I demonstrated a Gajillionitem element generator expression in my shell, but used brackets instead of parenthesis.

Decorators
------------

* Expressive
* Easy on the eyes
* Works for functions, methods, and classes
* Adds powerful layer of composable tools

Abstract Base Classes
-------------------------

Uniform definition of what it means to be a sequence, mapping, etc

Ability to override is `isinstance()` and `issubclass()`

* The new duck-typing "If it says it's a duck..."

Mix-in capability

Superstars
-----------

Unbelievably good people coming into things


Guido Van Rossum
===================

Forthcoming

Van Lindburgh
================

Forthcoming
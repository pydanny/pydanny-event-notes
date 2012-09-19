==========================================================================
What I missed about Python (and how JS taught me to love Python even more)
==========================================================================

* by Audrey Roy

    * https://twitter.com/audreyr
    * http://audreymroy.com
    * PSF Member
    * My fiancee!
    
Description
============

What happens when you take a Python developer and immerse her completely in JavaScript for a few weeks? This talk tells the story of my journey through JavaScript, from deep-diving in and looking for Python analogues in JS to achieving a greater understanding and appreciation of Python's design through comparative language study.

.. note:: Spent the talk taking pictures. Waiting for some notes taken by others that I'll be including here.



Background
----------

PyLadies, OpenComparison, PyCon Phillipines


Total immersion in javascript
-----------------------------

Several weeks of intense JSing

"JS is a terribly misunderstood language"

Pre-Immersion:
 python is better
 js is invevitable

Is JS good parts is good enough to just work with it?

Is it worth it?
 use ajax more?
 use full blown python soa and backbone.js?
 integrate js relatime features?
 
JS spectrum: 
  avoid at all cost <---> Happiliy use 100% JS

Findings
--------

Python is elegant!
  good parts included (in js not so readily)

JS ecosystem is thriving
  works where python ecosys does not
  very ambitious


Funcions in python
  intedentation begets clarity of scope
  docstrings, named parameters
  minimizing anonymous funs
  
Funcitions in JS
  the infamous 'var'
  anonymous function... not
  no default params
  worse documentation tools
 
JS is more functional, and thus better. Right?
  closures as solution for scope leakage
  closures as classes
  closures as modules

(Audrey had an error on her slide, as if to emphasise
cumbersomnes of JS closure hacks).

Functional programing in python
  iterators, generators
  list comprh.
  batteries included (itertools, functools, operator)

Lambdas -- anonymous funcs are by design constrained.
 
You can nest functions in python has much more sense.

What python cant do?
  close over a non-global var in outer scope (python 3)

Python classes are elegant!
  scope is obvious
  class is namespace
  docstring
  
Klass in JS:
  at least two different hacks
  not one obvious way
  prototypal inheritance is complex
  different is not always better
  reallity: prototypal is annoying

Modules:
  long history in python
  simple, defined by files
  
Modules in JS:
  just a script tag
  not part of the language, some libraries provide shim

Packaging
  no one true way in python, confusing
  
Packaging JS:
  many alternatives: npm, ender, jam, bower
  not build into the lang

Code reuse 
  two obvious necessities
  importing libraries
  organizing code int o dierctories

Design patterns
  classes provided by language
  decorators
  iterators and gens
  modules
  
  pthon minimizes boilerplate
  js brings DP with libraries, many times

Standard library
  python has great stdlib, with some parts dated; opinionated
  js has none; jQuery, Node, no strong leadership

Stdlib - datetime
  js date.js died, although it was touted as best
  python datetime has limitations, but it's there
  some good js libs exist, but lack recognition

JS and polyfills
-----------------

  hack away what is not defined

JS beats Python (reality wins)
------------------------------
  js working in browser
  cross platform mobile dev tools
  huge innovation

Summary
-------
  Python has good parts emphasised
  but has catching up to do

*You should try diving deep into JS.*


Diversity helps community!
--------------------------
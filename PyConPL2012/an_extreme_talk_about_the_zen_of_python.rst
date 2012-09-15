=======================================
An extreme talk about the Zen of Python
=======================================

 * by Daniel Greenfeld
 
Description
===========
 
In the Python community we are taught from the outset of learning the language that the Zen of Python serves as a guide for how we should construct our codebases and projects. Rather than go into the zen-like meanings of each statement, this talk will explore how individual koans are implemented via detailed displays of sophisticated code examples.

Introduction
============

No easy code examples, Daniel's gonna show some twisted, complicated code.

Daniel's grandparents come from Dynów, Poland. (Applause)

He was a Python programmer at NASA and later started consulting work.

Met @audreyr at PyCon 2010. 

Runs some opencomparison sites - djangopackages etc.

The Zen of Python
=================

Written by Tim Peters, author of timsort algorithm - a really smart guy according to Daniel. 

The Opening
===========

    Beautiful is better than ugly.
    Explicit is better than implicit.
    Simple is better than complex.
    Complex is better than complicated.
    Flat is better than nested.
    Sparse is better than dense.
    Readability counts.

Demonstrated using ``super()``.

Geometrical figures, ``Ring`` derives from ``Circle``. Obvious what ``super`` will do. But what if it wasn't so simple?

``super`` does things automatically and can lead to ambiguity.

    In the face of ambiguity, refuse the temptation to guess.
    
Absolutely inheriting __init__ from base class: explicit, simpler, more readable.

Explicit > Implicit
===================

:: 
    Circle.__init__ > super()
    
Django CBVs
===========

Composition, inheritance, polymorphism and other funny words.

What's the ancestor chain to ``UpdateView``? Answer: 8 ancestors. Impossible to memorize what each of them does.

``form_valid()``, but which one? 

OMG! OMG! OMG! Even more mixins. Let's print the MRO. A screenful of ``<class '...'>`` follows.

Filter the list on classes which have ``form_valid()`` method -> only 5 classes (*I was lucky*).

**MRO is simple, but simple is relative.**

Moving on
=========

Django controversy
==================

 * WSGI (fixed)
 * configuration and setup (working on it)
 * CBVs (working on it)
 * not MVC-compliant (and this is fine)
 
MTV != MVC

Is MVC applicable on the web?

The Zen of Python doesn't mention MVC.

Separation of presentation from content
=======================================

Django is fine. CBVs are not along the lines of Zen.

Controversy: web2py
===================

Implicit > explicit. 

Follows it's own design patterns.

Where are the imports? No imports neccessary. WAT?

.. note:: Nobody expected Spanish Inqusition!

web2py breaks 3 koans of the Zen. Implicit behaviors, ambiguity, namespaces.

*Although practicality beats purity.*

Easy to install, easy to learn, less boilerplate. Web2py <3 Windows.

Similar to Django in terms of contention and trackage.

Exceptions in exception handling
================================

Django Packages
===============

Updates metadata from PyPI, Github, Bitbucket. PyPI unstable, APIs change, projects get deleted etc.

First: concatenating some string with error messages from exception handlers. 

Traceback wanted. Type of the error, message, location.

Code is silent - for no good reason apart from laziness.

**Solution**: added logging in ``__init__`` in a custom ``Exception`` subclass.

Code is not silent anymore. Errors are noisy.

Cleaner code
============

Even more controversy. (*Unless you're Dutch*).

Decorators
==========

Decorators are easy to explain! 

Wrapper function running code before/after the decorated function.

Getting harder to explain... closures etc.

Now let's talk about decorators with arguments. *general laughter*

Danny is evil, uses confusing names: ``multiplier``, ``multiple``...

Whew.

Don't forget ``functools.wraps``. The decorator code in the slides is growing like a tumor.

*It's not easy to (explain how to) write decorators.*

But decorators are awesome! Using them is like Zen, writing is not.

The last section
================

Getting it done vs technical dept
=================================

Tests & docs take time. Do we have to do them? Maybe not. But it brings a lot of risks.

Must-have docs
==============

 * installation/deploy
 * coding standards
 * how to run tests
 * version information
 
Test patterns
=============

Test harness must at least run even without tests.

Use tests, not shell/repl.

Use coverage, reject code that drops coverage.

Don't use doctests.

Namespaces
==========

Powerful, useful, precise.

``import *`` makes development faster. IMPORT ALL THE THINGS!

Confusing imports, same names in ``os`` and ``re``. Subtle trouble!

Replaces things from in ``builtins`` (``os.open`` breaks ``open``)

The ``open()`` story
====================

``os.open`` needs different arguments than ``open``. You're screwed if you confuse these calls.

COntention
==========

``import *`` is for people who know what to do.

Remember ``__all__``.

Summary
=======

The Zen of Python (repeated)

One more thing
==============

Capoeira moves!


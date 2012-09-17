================================
Extreme Talk about Zen of Python
================================

.. note:: live-noted by Łukasz Langa (ambv) and submitted as a pull request

"What mistakes I did and how I correct them."

The speaker: Daniel Greenfeld, both his parents' ancestors were from Poland. Learned Python at NASA.

Tim Peters is the author of "Zen of Python", also known for Timsort.

The Opening:
------------

* Beautiful is better than ugly.

* Explicit is better than implicit.

* Simple is better than complex.

* Complex is better than complicated.

* Flat is better than nested.

* Sparse is better than dense.

* Readability counts.

Example 1:
~~~~~~~~~~

The ``super()`` method is doing things automatically and can create ambiguity.
It doesn't adhere to the Zen of Python by being implicit.

Moreover:

* If the implementation is hard to explain, it's a bad idea.

* If the implementation is easy to explain, it may be a good idea.

Example 2:
~~~~~~~~~~

The ancestor chain of ``django.views.generic.edit.UpdateView`` is very long (8
ancestors or so)::

  >>> pprint.pprint(UpdateView.mro())
  [<class 'django.views.generic.edit.UpdateView'>,
   <class 'django.views.generic.detail.SingleObjectTemplateResponseMixin'>,
   <class 'django.views.generic.base.TemplateResponseMixin'>,
   <class 'django.views.generic.edit.BaseUpdateView'>,
   <class 'django.views.generic.edit.ModelFormMixin'>,
   <class 'django.views.generic.edit.FormMixin'>,
   <class 'django.views.generic.detail.SingleObjectMixin'>,
   <class 'django.views.generic.edit.ProcessFormView'>,
   <class 'django.views.generic.base.View'>,
   <type 'object'>]

Readability counts and this is not readable:

* it is very hard to actually remember what each mixin does

* they can have non-obvious side effects

Possible mitigations for this view
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* leave it as it is

* use concrete parent class methods instead of ``super()`` (bad idea)

* rebuild it to use functional views

* increase awareness of the design, simplify it, document it in detail

Controversies
-------------

* Special cases aren't special enough to break the rules.
  
* Although practicality beats purity.

Django
~~~~~~

Django is pretty good about following the Zen of Python.

* WSGI
  
  * fixed

* Class-based views are too complicated (versus complex)

  * author works on document them better and simplify where they're too
    complicated

* Not MVC compliant

  * not a concern because what matters is separation of data and presentation

web2py
~~~~~~

Web2py argues practicality in some very specific places, will always be
contentious.

* "Explicit is better than implicit." - has implicit imports

  * On the other hand this implicitness makes it easier for beginners.

  * The namespace pattern is easy to learn.

  * Imports are boilerplate.

* "In the face of ambiguity, refuse the temptation to guess."

Exception handling
------------------

* Errors should never pass silently.
  
* Unless explicitly silenced.

Story: Django Packages. Once a day iterates across all packages. Updates the
metadata from multiple sources. Sometimes the APIs go down or change. Sometimes
objects get deleted. Sometimes network connectivity fails.

The first approach to a solution of these problems was to catch a bare
``Exception`` and print it out. Problems:

* the code is nearly silent: printing the exception causes the stacktrace not to
  appear

* ``print`` as a logger

More controversy 
-----------------

* In the face of ambiguity, refuse the temptation to guess.

* There should be one-- and preferably only one --obvious way to do it.

* Although that way may not be obvious at first unless you're Dutch.

Decorators are easy to explain for the user, not so much for the implementer.
Especially if they should accept arguments. And don't forget about
``functools.wraps``. Etc. etc.

Using decorators is like Zen. Writing decorators is not.

Decorator Template
~~~~~~~~~~~~~~~~~~

.. sourcecode:: python 

    def decorator(function_to_decorate):
        def wrapper(*args, **kwargs):
            # do something before invoation
            result = func_to_decorate(*args, **kwargs)
            
            # do something after
            return result
        # update wrapper.__doc__ and .func_name
        # or functools.wraps
        return wrapper
        
.. sourcecode:: python 

    # class as a decorator
    class decorator_class(object):
        def __init__(self, function):
            self.function = function
        def __call__(self, *arg, **kwargs):
            result  = self.function(*arg, **kwargs):
            # do stuff to result
            return result
            
    @decorator_class
    def hello():
        return 'hello'

On one hand:

* If the implementation is hard to explain, it's a bad idea.

* If the implementation is easy to explain, it may be a good idea.

On the other:

* Practicality beats purity.

Final section
-------------

Some things can take time like tests or documentation. You can skip them risking
multiple coding standards, deploying broken code or problems upgrading
dependencies. So if you have to skip documentation, at least write down:

* installation/deployment procedures

* coding standards

Easy test patterns for developers racing to meet deadlines:

* always make sure your test harness actually runs even if you don't have tests
  yet

* try using tests instead of shell/REPL

* after the first deadline, reject any incoming code that drops coverage

* use ``coverage.py``

Namespaces
~~~~~~~~~~

* Extremely powerful

* Useful

* Precise

Beware: ``from ... import *`` makes development faster but it can be dangerous::

  import re
  import os

  # clashing names!
  assert re.sys == os.sys
  assert re.error != os.error

  # clashing builtins!
  assert re.compile != compile
  assert os.open != open

So don't do ``from re import *``, etc. Especially, ``import *`` is not for
beginners. If you do know Python and know about ``__all__``, etc. you might use
it if you're careful.

Summary
-------

.. sourcecode:: python 

  >>> import this

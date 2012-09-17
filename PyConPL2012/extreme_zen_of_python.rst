=======================================
An Extreme Talk about the Zen of Python
=======================================

.. note:: live-noted by Audrey Roy (audreyr) and submitted as a pull request

Daniel Greenfeld
----------------

* Family on both sides from Poland
* Principal at Cartwheel Web, PSF & DSF member
* Fiancee is @audreyr!
* Co-lead on OpenComparison which powers djangopackages.com and more

Zen of Python
-------------

* By Tim Peters, author of Timsort which is used everywhere
* Extreme examples of each follow

super()
-------

* Built-in method
* Walkthrough of circle-ellipse problem
* Can create ambiguity
* Hard to remember syntax for super()
* Circle.__init__(self, outer) is more explicit and simpler
* Explicit is better than implicit

Django CBVs
-----------

* Quiz: What is the ancestor chain for django.views.generic.edit.UpdateView?

    * Answer: There are 8 things. Hard to remember what each ancestor does.

* In super(ActionUpdateView, self).form_valid(form), which form_valid() is being called?
* If not careful, super() can cause MRO problems
* Possible mitigations:

    * Hope maintainers aren't angry
    * Convert to functional view
    * Explore better patterns

Django
------

* Special cases aren't special enough to break the rules, although practicality beats purity
* WSGI is fixed
* Config & installation - working on it
* CBVs - working on it
* Not MVC.  Model-Template-View. Web not necessarily appropriate for MVC.

Web2py
------

* Where did the response object come from?
* 3 koans broken:

    * Explicit is better than implicit
    * In the name of ambiguity, refuse the temptation to guess
    * Namespaces are good...

* In their case, it's a design decision. "Practicality beats purity"

    * Easier for beginners
    * Easy to learn their namespace pattern
    * For experienced devs, saves boilerplate

* Web2py's easy installation process is where they shine

OpenComparison
--------------

* Example showing a general exception
* http://bitly.com/????
* By printing (e), you don't get the error type or stack trace
* Fixed code with a custom exception that gets raised and prints additional info

Decorators
----------

* Awesome to use
* Easy to explain what they do
* He did a walkthrough of a sample decorator without arguments.  Then one that accepts an argument.

    * 3 nested functions
    * Hard to read

* He corrected himself because he didn't use @functools.wraps, which is the better way to define decorators. More complexity.
* Hard to explain implementation
* If the implementation is hard to explain, it's a bad idea. If the implementation is easy to explain, it may be a good idea.

Getting it done vs. technical debt
----------------------------------

* Tests and docs take time. Skipping them risks:

    * Multiple coding standards
    * Deploying broken code
    * Problems upgrading dependencies
    * Forgetting install/deploy

* Must document:

    * Installation/deployment
    * Coding standards
    * How to run tests
    * Config

* Easy test patterns:

    * Always make sure test harness can run
    * Use tests instead of shell/repl
    * After 1st deadline, reject incoming code that drops coverage
    * Use coverage.py

Namespaces
----------

* Powerful, useful, precise
* Dangerous to use `import *`

.. code-block:: python

    >>> from re import *
    >>> from os import *

    >>> re.error == os.error
    False

Breaking built-ins
------------------

Continued from above:

.. code-block:: python

    >>> compare_builtins(re)

* Breaks compile() built-in

.. code-block:: python

    >>> compare_builtins(os)

* Breaks open() built-in

* Bad shortcut pattern to teach beginners. Technical debt.

Summary
-------

* Our community is built off of the Zen of Python
* Thank you: Richard Jones, Raymond Hettiger, Matt Harrison, Kenneth Love, PyCon Poland, others

=================
Ur doing it wrong
=================

by James Bennett
~~~~~~~~~~~~~~~~

Our WVA friend

To start off: RTFM
~~~~~~~~~~~~~~~~~~

#. People starting Django often don't have a background in Python.
#. Perl maxim #11924 "Well, if you don't know what it does, why did you put it in your program?"
#. Get the basic python bits down


Idea: Django module of the week
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. Just like Doug Hellman's Python module of the week
#. Would take 2 years
#. The problem is that I need a better blog engine

Django is just Python
~~~~~~~~~~~~~~~~~~~~~~

#. Django applications are just python modules. Did not reinvent the wheel.
#. Django Views could be callable classes. Hmmmm...
#. Django admin used callable classes for views.
#. Yet people never grok that Django is really just python. 

The biggest problem with the perception of Django
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

People think that Django is too glued together. But that isn't true:

#. Just do `import SqlAlchemy`
#. You don't need to use Django's default components


.. note: We used RSA and a SOAP service for auth in Django at NASA. Which in both cases was sucky. Hates RSA and SOAP I do!

Testing new Django apps
~~~~~~~~~~~~~~~~~~~~~~~~~~

What James does to check out your app:

#. Need to have your stuff working with standard Django install tools.
#. top level stuff needs to be there in your package.
#. Stay away from setuptools. Go to `distribute` by Tarek Ziade
#. Wants to see a concise one-sentence explanation from the README describing what the app does
#. You better have a good explanation as to why you are duplicating other person's work
#. Wants to see documentation or will file a bug. Will jump away from your work if you don't have it unless you are lucky.
#. Pick a license. Choosing one causes a flame. Django prefers the BSD.
#. Tests are handy. If there aren't unit tests he doesn't trust your code.

What turns off James:

#. Put this module in django.contrib
#. Ignoring standard features of Python or Django is silly

Something cool:

#. django-lint looks awesome
#. pypants is awesome
#. Assigns a score represented by pants on Python packages

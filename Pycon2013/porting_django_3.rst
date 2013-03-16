================================
Porting Django apps to Python 3
================================

Django 1.5 now supports Python 3, so now's the time to start thinking about porting your apps and sites. Come see how! I'll talk about the porting techniques that work, and present two case studies: porting a site, and porting a reusable app.

by Jacob Kaplan-Moss

    * Django co-creator and BDFL
    * https://github.com/jacobian / https://twitter.com/jacobian


Do I want to use Python 3?
=============================

Python 3 has fewer warts

* `urllib` / `urllib2` replaced with `urlparse`
* std library cleanup
* funky syntax is killed
* `print()` is a function!
* `super()` syntax is better!
* unicode no longer sucks!

Can I use Python 3?
=====================

A solid maybe. Missing pieces as of 3/16/2013:

* No Python Image Library (PIL / Pillow)
* No MySQL python 3 bindings aren't that good.
* Popular items on https://www.djangopackages.com:

    * No gunicorn as async (sync does work)
    * No django-debug-toolbar
    * No django-registration
    * No django-extensions
    * No Haystack
    * No django-tagging
    * No Sentry
    * No django-compressor
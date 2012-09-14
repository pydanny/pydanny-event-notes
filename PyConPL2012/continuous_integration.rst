================================================================================
Continuous integration - czyli jak spędzić weekend z dziewczyną zamiast z szefem
================================================================================

by Łukasz Langa

.. note:: Alas, I got convinced to try doing this late. And I don't speak Polish. 

Description
============

Większość z nas woli programować zamiast debugować. Tym bardziej mało kto lubi szukać błędu na serwerze produkcyjnym w sobotni wieczór. Jak tego uniknąć? Nie wpuszczaj błędów na produkcję. Podczas prezentacji pokażę jak przy użyciu takich projektów jak nose, jenkins, pyflakes, fabric tego dokonać.

This is a talk on continuous integration and best practices.


Pyflakes and PEP-8
==================

* Use tools to validate the quality of your code
* Develop good habits

Coverage.py, nose, and other tools
===================================

* coverage.py lets you know how much is tested
* nose discovers tests.


Automatic Installation
======================

* Create a reproducable installation procedure that is executed via tools
* Don't do it manually

Useful tools include:

* Fabric
* Pip
* Virtualenv

Set up your own QA servers
===========================

* Set up your own servers takes a lot of work and effort.
* OpenStack is nice because:

    * It does a lot of the lifting for you
    * Open source so you can use it for free and contribute back

* My Polish is bad so I wonder if I missed him suggesting paid PaaS like Heroku, dotCloud, et al


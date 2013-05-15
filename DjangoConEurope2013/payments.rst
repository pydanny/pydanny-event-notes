============================================
Processing payments for the paranoid
============================================

* By Andy McKay

    * @andymckay
    * Works at Mozilla
    * Presented barefoot

The Mozilla Marketplace is the app store for Firefox OS and this Django powered site takes payments from users. 

Combined with issues like localisation, identity and scale - we are processing payments through Django. This talk will cover the marketplace, the architecture of the system and how we cope with all the paranoia.

Who should be paranoid?
========================

Everyone should be paranoid:

    * Developers
    * Users
    * banks
    * Everyone
    
Mozilla Marketplace
=====================

* Powered by Django
* Don't call it an "app store"
* accepts payments
* Powered by open source project 'zamboni'

.. note:: 

    Report bugs to Mozilla via their reporting system and they'll pay you.

Steps for purchase
=====================

1. Set up your account with Mozilla
2. Purchase and use an app
3. Mozilla bills your carrier

All powered by Solitude: https://github.com/mozilla/solitude

Vulnerabilities they had to consider
========================================

XSS
---

Over come with 
* Mozilla Content Security Policy
* MDN_ docs
* Github blog

Phishing
------------------------

* navigator.mozPay
* Trusted UI
* MDN_ docs

SQL injection
--------------

* careful ORM evaluation

Ourselves
-----------

* Many penetrations happen internally, not from technical assaults from outside.
* Wrote anonymizing code
* Inside the DB:

    * removed personally identifying information
    * encrypted other data
    
* Defended by depth

Tips
==============

* use python-requests

    * SSL certs are not handled well by Python's URLLIB
    * Requests does it well
    
* OWASP
    
    * django-paranoia

.. _MDN: https://developer.mozilla.org/en/docs‎


.. note::

    Just noticed that @andymckay is presenting barefoot at @djangocon @djangofact #djangocon

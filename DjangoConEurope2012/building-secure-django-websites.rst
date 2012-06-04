===============================
Building secure Django websites
===============================

* by Erik Romijn

    * hello@solidlinks.nl
    * http://twitter.com/erikpub
    * slides: https://speakerdeck.com/u/erik/p/building-secure-django-websites

Three Areas
============

* Integrity

    * Internal consistency or lack of corruption in electronic data

* Confidential

    * To keep data secret that was intended to be secrity

* Available

    * ability to be used or obtained
    
How cookies and sessions work
==============================

.. parsed-literal::

    Set-cookie: name: value
    Cookie: name=value
    
Sessions
----------

.. parsed-literal::

    sessionid=8f70xxxxa3d9
    session: {
        key: 8f70xxxxa3d9,
        user: Erik
    }

If you can access the session of another user, you can impersonate the other user.    

Cross Site Request Forging
---------------------------

Fortunately for us, if you use POST, Django by default has CSRF protection enabled via:

.. code-block:: django

    <form>
        {% csrf_token %}
        ....
    </form>    

XSS Injection
==============

Injecting HTML or JavaScript into things like field data

.. code-block:: html

    <p>Injecting issues <script>alert("I'm a JavaScript injection!");</script></p>
    
Reflected vs. Stored XSS
==========================

* Previous examples are reflected XSS

    * Have to try the user into visiting my link
    
* Other possibility is stored XSS

    * Store some data which is later sent back to users, e.g. blog comments
    
Cookie security
================

* HTTPOnly flag will prevent reading cookie from JS
* Alternate attack is Cross Site Tracing (XST): disable TRACE on your web server
* Note: if cookie domain is set to e.g. djangocon, every website under djangocon.eu is at risk.

Server side injections
=======================

SQL injection
--------------

* No concern, Django ORM prevents injection
* If you don't use it, stick to prepared statements

LDAP Injections
-----------------

* You can play creative games if you know the LDAP specification

.. note:: I saw this at NASA HQ before we rolled out my first professional Python application back in 2006.

Shell Injection
----------------

* Always use ``subprocess``

Trusting the Browser
=====================

* The browser is under the user's control
* Which means you cannot trust anything that the user is doing

Be careful with ModelForms
==============================

Don't use the `exclude` Meta attribute in ModelForms!

.. code-block:: python

    class Profile(models.Model):
        user = ForeignKey(User)
        phone = models.CharField()
        is_admin = BooleanField() # added later
        
    class ProfileForm(ModelForm):
        model = Profile
        exclude = ('user', )
        
.. code-block:: django

    <form>
        {{ form.non_field_errors }}
        Phone: {{ form.phone }}
    </form>

Passwords and SSL
==================

* Don't use plaintext passwords
* Limit the number of attempts (django-axes, django-lockout)
* If you use logins, use SSL
* If you use SSL, look at django-secure

Clickjacking and Django
=========================

* Protection in Django 1.4
* django.middleware.clickjacking
* etc

Backups
=========

* Run backups
* If you don't have backups, who owns your stuff?
* Test your restores!
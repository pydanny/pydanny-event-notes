========
Security
========

.. note:: Had some things to do so did not get a chance to focus on this talk

by Paul McMillon

 * Security expert since 1998
 * Just now a core developer of Django
 
SSL - safe and secure
=========================

**Are you doing it right?**

 * Standard way is to redirect from HTTP to HTTPS
 * That doesn't stop images on HTTP from sneaking in cookies
 * Use HTTPS secure cookies!
 * Use HTTP Strict Transport Secruity (HSTS)
 
Use django-secure
------------------

 * Identifies these issues
 
 
Don't put your database in your github repo
================================================

 * Django needs better hashing
 * Even on open source projects
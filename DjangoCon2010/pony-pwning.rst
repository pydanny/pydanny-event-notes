======================================
pony pwning
======================================

By Adam Baldwin

He breaks stuff. He hack and cracks. And gave a really useful talk!

Notes
=====

**django** = pile of *awesome*

*Django has good security*

Developers aren't perfect
=========================

Don't rely on QA to find your bug

Security Failures minority issues
------------------------------------

30% based on incompetence or ignorance
9% based are needle in haystack code issues (XSS)
1% are 0 days

90% of the problems
-------------------

XSS issues
~~~~~~~~~~~~

 * Template system issues

   * autoescape off, safe, mark_safe
   
   * context HTML
  
 * IE has security holes.
 
Avoid getting burned

 * Consider OWASP ESAPI
 * Audit templates
 * Audit reusable and snippets
 * Educate designers
 
File uploads
~~~~~~~~~~~~

 * images can contain PHO
 * ImageField does not case
 * Image field does not check extensions
 * File uploads often are put in unprotected directories
 
Direct Access is bad
~~~~~~~~~~~~~~~~~~~~

Return a Not Found error if people can't find something and log the exception

Doing stupid things
~~~~~~~~~~~~~~~~~~~

Priviledged operations with HTTP GET

eg /object/delete/2 is bad!

Also, don't expose IDs

Click Jacking
~~~~~~~~~~~~~

/admin/ **was** vulnerable. This has been fixed as of Django 1.3

Mitigations:

 * Set X-FRAME-OPTIONS DENY header
 * Use django-xframeoptions middleware
 * Implement frame breakout code

admin
~~~~~

 [Redacted]
 
Communicate with security guys
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 * They are impatient
 * Will publish it if you do not respond/fix
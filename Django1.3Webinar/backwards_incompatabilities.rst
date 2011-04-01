==============================
Backward Incompatible Changes
==============================

Usually because of security or database bugs. Sometimes the docs were wrong.

Security Fixes
================

 * Added CSRF validation for AJAX requests - Done to protect FLASH, not browsers.
 
    * Symptom: Posts request will fail .
    
 * Placed restrictions on filters in the admin
 
 * Stopped rendering passwords in PasswordInput
 
 * Users that are inactive can't reset their passwords anymore
 
AJAX specifics
===============

http://django.me/csrf-ajax::
 
    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!(/^http:.*/.test(settings.url) || /^.test(settings.url))){
                // Only send the token to relative URLs i.e. locally.
                xhr.setRequestHeader("X-CSRFToken",
                    $("csrfmiddlewaretoken").val());
            }
        }
    });
    
Data-loss bug
=============

File field deletion issue (Look up in Jacob's slides!)

Optimizations
=============

 * manually managed transactions (via @transaction.commit_manually) needs to be explicitly closed
 * New index on session table::

    python manage.py sqlindexes sessions
    
        * But Jacob recommends using memcached or redis sessions for performance on sites with huge numbers of frequent users.
        * Google on django-redis-session

The rest
========

 * Clearable FileField widget is the default
 * No more PROFANITIES_LIST (re-set to get the old behavior)
 * Localflavor corrections for Canada, Indonesia, and the USA
 * FormSets can no longer take empty data
 * Iiitial SQL no longer works in tests. Use fixtures instead.
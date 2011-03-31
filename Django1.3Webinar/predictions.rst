====================
Predictions for 1.4
====================

To be removed
-------------

 * Python 2.4 support
 * Remaining single-db support
 * Old style messages are going away
 
    * Don't use django.contrib.auth.messages!
    * Use new messages (django.contrib.messages)
    
 * Legacy auth backends are going away

See http://django.me/depreciation

Rampant Speculation
-------------------

 * Basic schema migration support
 * Refactor and formalization of "apps"
 * Improved ideas of what a "user" is
 * Better hooks for monitoring, debugging, and metrics
 * template compilation
 * Better time zone support
 * Python 3

====================
Predictions for 1.5
====================

Possible removals
-------------

 * Python 2.5 support (2.6 is just plain faster)
 * mod_python support (no more support, no way to download, just say no!!!)
 * Removal of function based generic views
 * Old-style url and ssi template tags
=================================================
Healthy Webapps Through Continuous Introspection
=================================================

by Erik van Zijst

* http://twitter.com/erikvanzijst
* https://bitbucket.org/evzijst

Case study: Wasted cycles on Bitbucket
=======================================

``=> SSHD => conq (Python) => git/hg``

* conq is our custom SSH shell
* conq imports Django ORM and Bitbucket code
* takes ~1.41 seconds to start (spawns ~50/second)

Solution after analysis: Stop the imports and just write native SQL
----------------------------------------------------------------------------

* 16 times faster to start up (0.09s vs 1.41s)
* 60% load decrease on all web servers!

Lessons learned
----------------

* Test your stuff
* Monitor your servers

Common problems
===============

Slowness in Web Apps
---------------------

* Slow SQL queries (or too many!)
* lock contention

    * between threads
    * database table/row locks
    * fine locks (git/hg)
    
* excessive IO (disk/network)
* evil regex: ``r'^(a+)+$'``

consequences
--------------

* 503 - worker pools full
* 500 if requests time out (Gunicorn SIGKILL)

The latter is best avoided as it destroys forensic evidence and leaves stale state (e.g. lock files)

Dogslow
========

* Django middleware
* emails tracebacks of slow requests
* no performance penalty, safe on prod
* https://bitbucket.org/evzijst/dogslow

django-geordi
==============

Designed to profile your production environment without impacting performance

* selectively profile individual requests
* add "?__geordi__" to any URL
* products PDF call graph
* https://bitbucket.org/evzijst/django-geordi

interruptingcow
==================

Designed to let you catch and then bubble up a system locking issue

.. code-block:: python

    import re
    from interruptingcow import timeout
    
    try:
        with timeout(20.0, RuntimeError):
            #evil regix
            re.match(r'^(a+)+$', 'aaaaaaaaaaaa')
    except RuntimeError:
        print 'Interrupted'
=================================================
Healthy Webapps Through Continuous Introspection
=================================================

by Erik van Zijst

* http://twitter.com/erikvanzijst
* http://butbucket.org/evzijst

Case study: Wasted cycles on Bitbucket
=======================================

=> SSHD => conq (Python) => git/hg

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
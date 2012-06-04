=========================================
10 Steps to better postgresql performance
=========================================

* Christophe Pettus
* PostgreSQL guy
* Done PostgreSQL for over 10 years
* Django for 4 years
* Not going to explain why things work great, just will provide good options. Ask him later for details

.. note:: Christophe talks super fast and I can't keep up

PostgreSQL features
====================

    * Robust, feature-rich, fully ACID compliant database
    * Very high performance, can handle hundreds of terabytes
    * Default database with Django
    
PostgreSQL negatives
====================

 * Configuration is hard
 * Installation is hard on anything but Linux
 * Not NoSQL
 
Logging
========

* Be generous with logging; it's very low-impact on the system
* Locations for logs

    * syslog
    * standard format to files
    * Just paste the following:
    
.. parsed-literal::

    log_destination = 'csvlog'
    log_directory = 'pg_log'
    TODO - get rest from Christophe
    
Shared_buffers
================

TODO - get this

work_mem
========

* Start low: 32-64MB
* Look for 'temporary file' lines in logs
* set to 2-3x the largest temp file you see
* Can cause a **huge** speed-up if set properly
* Be careful: it can use that amount of memory per query

maintenance_work_mem
=====================

* Set to 10% of system memory, up to 1GB

effective_cache_size
======================

* Set to the amount of file system cache available
* If you don't know it, set it to 50% of the available memory

Checkpointing
================

* A complete fish of dirty buffers to disk
* Potentially a lot of I/O
* Done when the first of two thresholds are hit:

    * A particular...
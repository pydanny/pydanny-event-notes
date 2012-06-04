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
 

Configuration
===============
 
Logging
-------

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
--------------

TODO - get this

work_mem
--------------

* Start low: 32-64MB
* Look for 'temporary file' lines in logs
* set to 2-3x the largest temp file you see
* Can cause a **huge** speed-up if set properly
* Be careful: it can use that amount of memory per query

maintenance_work_mem
---------------------

* Set to 10% of system memory, up to 1GB

effective_cache_size
---------------------

* Set to the amount of file system cache available
* If you don't know it, set it to 50% of the available memory

Checkpointing
--------------

* A complete fish of dirty buffers to disk
* Potentially a lot of I/O
* Done when the first of two thresholds are hit:

    * A particular...

.. note:: Didn't get any of this part of things.

Easy performance boosts
=========================

* Don't run anything else on your PostgreSQL server
* If PostgreSQL is in a VM, remember all of the other VMs on the same host
* Disable the Linux OOM killer

Stupid Database Tricks
----------------------

* Don't put your sessions in the database
* Avoid aonstantly-updated accumulator records.
* Don't put the task queues in the database
* Don't use the database as a filesystem
* Don't use frequently-locked singleton records
* Don't use very long-running transactions
* Mixing transactional and data warehouse queries on the same database

One schema trick
-----------------

* If one model ha sa constantly-updated section and a rarely-updated section

    * last-seen on site field
    * cut out that field into a new model

SQL Pathologies
-----------------

* Gigantic IN clauses (a typical Django anti-pattern) are problematic
* Unanchored text queries like '%this%' run slow

Indexing
---------

* A good index

    * Has high selectivity on commonly-used data
    * Returns a small number of records
    * Is determined by analysis, not guessing

* Use pg_stat_user_tables - shows sequential scans
* Use pg_stat_index_blah

Vacuuming
----------

* autovacuum slowing the system down?

    * increase autovacuum_vacuum_cost_limit in small increments
    
* Or if the load is periodic

    * Do manual VACUUMing instead at low-low times
    * You **must** VACUUM on a regular basis
    
* Analyze your vacuum

    * Collect statistics on the data to help the planner choose a good plan
    * Done automatically as part of autovacuum
    
On-going maintenance
======================

keeping it running

monitoring
-------------

* Keep track of disk space and system load
* memory and I/O utilization is very handy
* 1 minute bnts
* check_posgres.pl at bucardo.org

pg_dump
--------

* Easiest backup tool for PostgreSQL
* Low impact on a running database
* Makes a copy of the database
* becomes impractical for large databases
=========================================
10 Steps to better postgresql performance
=========================================

* Christophe Pettus
* PostgreSQL guy
* Done PostgreSQL for over 10 years
* Django for 4 years
* Not going to explain why things work great, just will provide good options. Ask him later for details

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
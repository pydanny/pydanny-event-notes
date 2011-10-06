================================================
Processing Firefox Crash Reports With Python
================================================

* by Laura Thomson

    * Web tools engineering manager
    * author of two books:
    
        * MySQL
    
    * Done about 100 talks!
    * Mozilla is hiring like crazy

Overview
=========

    * The basics
    * The numbers
    * Work process and tools

The Basics
============

* Socorro crash information collector thingee
* Lots of companies use it to track this data:

    * Steam (game stuff)
    * Other things

How crashy is the browser?
--------------------------

* Mozilla Crash report - please use it!
* Will email you if you have malware they detect
* Generates https://crash-stats.mozilla.com/products/Firefox
* Mozilla needs your data to make Firefox better.

Basic Architecure
------------------

 * Database is PostGres
 * HBase for map-reduce, she wants to replace it with something else
 * Lots of components powered by Python
 * Front-end is PHP but will be converted to Django in 2012
 
Lifetime to a crash
--------------------

* Browser crashes
* Sends data to Mozilla in a big binary dump with a JSON header
* Mozilla processes the header and tries to generate a signature of the crash

    * They need more than just the function that created the crash
    * Doesn't cover all cases
    * Uses a regex to glean out other things from the binary crash dump

Back end processing
--------------------

Large number of cron jobs, e.g.:

    * Calculate aggregates: Top Crashers (Farmville if you want to know)
    * Process incoming builds from ftp server
    * Match known crashes to bugzilla bugs
    * Duplicate detection
    * Match up pairs of dumps (OOPP, content crashes, etc)
    * Generates extracts (CSV) for engineers to analyze
    
Middleware
-----------

* Moving all data access to be through REST API (by end of year)
* (Still some queries in webapp)
* Enable other front ends to data and us to rewrite webapp using Django in 2012
* Upcoming (2011 or 2012) each component will have it's own API

Webapp
------

* Hard parts: How to vizualize some of this data
* Ex: Nightly builds, moving to reporting in build time, not clock time
* Code crufty (old KohanaPHP)

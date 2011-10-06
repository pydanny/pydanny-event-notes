================================================
Processing Firefox Crash Reports With Python
================================================

* by Laura Thomson

    * Web tools engineering manager
    * author of two books:
    
        * PHP and MySQL Web Development
        * The Surrealists
    
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
====================================

* Mozilla Crash report - please use it!
* Will email you if you have malware they detect
* Generates https://crash-stats.mozilla.com/products/Firefox
* Mozilla needs your data to make Firefox better.

Basic Architecure
========================

 * Database is PostGres
 * HBase for map-reduce, she wants to replace it with something else
 * Lots of components powered by Python
 * Front-end is PHP but will be converted to Django in 2012
 
Lifetime to a crash
====================================

* Browser crashes
* Sends data to Mozilla in a big binary dump with a JSON header
* Mozilla processes the header and tries to generate a signature of the crash

    * They need more than just the function that created the crash
    * Doesn't cover all cases
    * Uses a regex to glean out other things from the binary crash dump

Back end processing
====================================

Large number of cron jobs, e.g.:

    * Calculate aggregates: Top Crashers (Farmville if you want to know)
    * Process incoming builds from ftp server
    * Match known crashes to bugzilla bugs
    * Duplicate detection
    * Match up pairs of dumps (OOPP, content crashes, etc)
    * Generates extracts (CSV) for engineers to analyze
    
Middleware
====================================

* Moving all data access to be through REST API (by end of year)
* (Still some queries in webapp)
* Enable other front ends to data and us to rewrite webapp using Django in 2012
* Upcoming (2011 or 2012) each component will have it's own API

Webapp
====================================

* Hard parts: How to vizualize some of this data
* Ex: Nightly builds, moving to reporting in build time, not clock time
* Code crufty (old KohanaPHP)

Implementation Details
====================================

* Python 2.6 mostly (PHP is the exception)
* Post Gres 9.1
* memcache for the webapp
* Thrift for HBase access

    * HBase is meant to work with Java
    * Could do it in Clojure/Scala but finding resources would be hard
    * Thought about Jython then backed off
    * Considering alternatives
* 100 users
* 100 Terabytes of data

Some Numbers
=============

* At peak 2300 crashes per minute
* 2.5 million per day
* Median crash size 150K, max size 20MB (reject bigger)
* ~110TB stored in HDFS (3x replication, ~40TB of HBase data)

What can they do?
==================

* Does a version of FF crash more than others?
* Analyze differences between versions of Flash
* Detect duplicate crashes
* Detect explosive crashes
* Find "frankenstalls" that can happen on Windows
* Email victims of malware

Implementation Scale
====================================

* > 115 boxes (not cloud cause that won't cut it)
* Now 8 devs + sysadmins + QA + Hadoop ops/analysts

    * Hiring: https://whitespacejobs.org

* Deploy approximatelt weekly but could do continuous if they need

Development Process
====================

* Fork
* Hard to install (must use VM)
* Pull request with bugfix/feature
* Code review
* Jenkins polls github master, picks up changes
* Jenkins runs tests, builds a package
* Package picked up and moved to dev
* Wanted changes merged to release branch
* Jenkins builds release branch, manual push to stage
* QA runs acceptance on stage
* TODO missing
* TODO missing

Absolutely Critical!
====================

**Build all the machinery for continuous deployment even if you don't want to deploy continuously**

* You don't want to install HBase

Upcoming
=========

* ElasticSearch implemented for better search
* More analytics; automatic detection of explosive crashes, malware, etc
* Better queueing
* Grand Unified Configuration System

Everything is Open Source
====================================

* https://github.com/mozilla/socorro

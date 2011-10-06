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

* Sorocco crash information collector thingee
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
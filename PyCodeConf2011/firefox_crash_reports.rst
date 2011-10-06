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
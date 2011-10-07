============
Breakdancer
============

* by Dustin Sallings

    * memcached contributor
    * http://dustin.github.com/    

* Does a lot of programming languages
* https://github.com/dustin/BreakDancer
* http://dustin.github.com/2010/10/27/breakdancer.html


Testing is a boring/hard subject
================================

* How do you find those edge cases?
* How do you detect crazy pairs of edge cases?
* Wait until there is a reported error?
* **pydanny contention: UnitTest makes it hard to document patterns in tests. User controlled**

Wrote a framework to help set tests
====================================

* Actions are the tests
* Drivers performs the tests and include specific conditions
* So that means your tests are independent of the conditions but defined in code?

.. note:: Seems like a design of separation of presentation from content in tests!!! MVC anyone?

MVC test framework? Pydanny Thoughts...
========================================

* Can this be implemented on top of UnitTest?
* If so, it can be back ported to other systems
* Not actually MVC, just a defined pattern
* BreakDance seems to generate code

Conclusions
=============

* Unit Testing isn't enough
* Find ways to detect and fire off edge case tests
* itertools will save you
* python makes otherewuse tedious tasks boring
============
Breakdancer
============

* by Dustin Sallings

    * @dlsspy
    * memcached contributor

* Does a lot of programming languahes

Testing is a boring subject
============================

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

* Can this be implemented on top of UnitTest? In which case, it can be backported to other systems

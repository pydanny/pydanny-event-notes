====================================
Testing: The Developer Strikes Back
====================================

.. note:: Sandy really, really, really rocked this talk

by Sandy Strong

 * Been doing Django since fall of 2009
 * Pyladies co-founder

Hard to do it right
====================

 * Delegate responsibilitiues correctly
 * wont always get it right first time
 * Presents reasons for refactoring
 * increases stability because you can test updates and patches
 
What is unit testing
====================

 * A unit is the smallest possible part of an application
 * Integration tests the whole and is often built out of unit tests
 
Practices
----------

 * Each class, method, and function should have its own test
 * Starting Django test.py files are limited
 * Organize however you want
 * Maintain consistency in your test patterns
 * Separate your tests between models, views, and hitting other services
 
    * keep things simple
    * easy to understand tests

* Don't keep all your tests into monolithic test.py files
* make multiple assertions



Mirror your project in your test layouts
============================================

.. note:: I love this pattern and use it myself!

 * Create test modules following the same file layout as your project
 * Have as few root test utils as possible 
 
    * Use it sparingly
    * just a few simple helper functions!
    
 * Your tests should copy the model/view/whatever tightly
 
Use ObjectCreator classes for mocks instead of fixtures
==========================================================

 * Mock your data by using the ORM or whatever persistence your system uses
 * Better than fixtures because mocking your objects this way means you are doing an addition ORM test
 * The `mock` library is supposed to be good

Beyond the business logic
===========================

 * Testing third-party libraries should be separate from other unit tests
 * Third party APIs go down. Even the big ones.
 * **Mock 3rd party API responses**
 * Means you can continue to work when Facebook, Google, et al go down

Dealing with cache
===================

 * Very hard
 * I tend to blow away the cache in a tearDown method
 * Her issues are beyond mine. Sandy rocks!
 
Writing tests can improve coding tests
========================================

 * Small functions can be tested. 200 lines functions cannot
 * Write more tests
 
    * Find good test patterns
    * Functions should perform a single function
    * Units of code should be true to the definition
    
What about T.D.D.?
==================

 * Step 1 - Write your tests
 * Step 2 - Then write the code

Sandy doesn't believe it exists.
--------------------------------

.. note::  I've done it for short periods.

 * Goes against prototyping
 * Requires full team buy0in to really work
 * Business owners rarely get it
 
Well tested code is often a happy medium
----------------------------------------

 * More realistic
 * More practical
 * Allows for a more individual style in coding 
 
Options to get people to test
============================================

 * webhooks tests to block code that isn't test
 * coverage.py makes it a game
 * Public shaming!
 
Junction between unit and integration
=====================================

 * Difficult areas to test because behavior is driven upon environment
 * Some code doesn't always work the way you want because people don't script/document things out

Testing a virgin codebase: 0-100%
====================================

 * You may find yourself faced with a project without tests
 * Set a pattern for tests, establish a framework follow it and get the team on board
 * Smaller tighter tests really help
 * Jenkins (continuous integration) is critical
 * Test Debt is part of Technical debt
 * Enforce the rule that **All future code MUST have tests**
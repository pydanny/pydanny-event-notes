=======
Testing
=======

Gem
---

 * fixtures = ['authtestdata']
 
Quotations
----------


Kent Beck::

    Tests are the programmer's stone, transmuting fear into boredom.

Microsoft Research::

    40-90% reduction in bugs takes 15-35% increase in time if you use Test Driven Development.
    
Jacob Kaplan-Moss::

    Whatever happens, don't let your test suite break thinging, "I'll go back and fix this later"
    
Django Tools
------------

 * Unit tests (unittest)
 * Doctests (doctest)
 * Fixtures
 * Test client
 * Email capture
 
Unit Tests
----------

 * Python 2.7 should support it much better 
 
django.test.TestCase
--------------------

 * Extends Python unittest
 * fixtures
 * Email capture
 * Database management
 * Slower than unittest.TestCase
 
doctests
--------

 * Neat
 * Eat to read
 * Hard to maintain
 
Functional Tests
----------------
 
 * a.k.a Behavior driven development
 * "Blackbox", holistic testing
 * Hardcore TDD folks look down on functional tests
 * But they keep your boss happy
 * Easy to find problems; harder to find the actual bug.
 
Fixtures
---------

Jacob like YAML over JSON because of readability. Don't bother with XML fixtures.
 
fixtures = ['authtestdata']

This is some basic Auth data from core that you can use to have groups and users. Hooray!

Test running::

    ./manage.py test
    ./manage.py test app
    ./manage.py test app.SomeTestCase
    ./manage.py test app.SomeTestCase.test_method    
    
New fixture tool
----------------

 * http://farmdev.com/projects/fixture
 * Content Types in fixtures
 
Coverage tool
-------------

 * Ned Batchelder's Coverage
 * http://nedbatchelder.com/code/coverage/
 * Coming in 1.2!
 
Mocking tool
------------

 * http://www.voidspace.org.uk/python/mock/
 
Browser Testing
---------------

 * Selenium (ya ya)
 * Windmill (has Django support now!)
 
Exotic Testing
--------------

 * Static source analysis (pylint is my favorite game)
 * Smoke testing via web crawlers (webcheck is my favorite)
 * Monkey testing aka fuzz testing
  
   * http://agiletesting.blogspot.com/2006/11/python-fuzz-testing-tools.html
   
 * load testing:
 
   * http://www.portswigger.net/suite/
   
Further resources
-----------------

 * http://bit.ly/py-testing-tools
 * http://us.pycon.org
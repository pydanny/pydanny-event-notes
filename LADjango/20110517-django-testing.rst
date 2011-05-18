==============
Django testing
==============

Sandy's great talk on test organization! I do things very similarly!

Organize and optimize your tests
===================================

* All apps need tests

* As your apps become more complex
    
    * test suite will grow larger
    * Increasingly complex test scenarios arise
    * seperate **code** and **service/infrastructure**
    
* Don't keep all your tests in one monolithic file named `test.py`

Don't do this
==============

 * Don't have a 6000 line test.py file! Break it down into `test_models`, `test_managers`, etc.
 
 * Don't test 3rd party APIs
 
    * Sandy prefers Mock and other faking of those systems
 
    * Danny: But how do you test your payment gateways and other API calls?
    
        * Paypal, Authorize.net
        * Github, Bitbucket, etc
        * Twilio, Tropo
        * Maybe have a stand-alone test suite called `third_party_apis`
 
Do this
========

sample of how I do it::

    core/
        tests.py # This is where my test utils go!
    myapp/
        tests/
            test_models.py
            test_views.py            
            
I prefix my test modules with `test_` so that way it is easier to identify them in various text editors. We already have enough models and views that it confuses me!

Sandy does things a bit differently, in that she calls test modules `models` and `views`. Really though, it is a measure of what you prefer for naming conventions

Dev environments and code testing
=================================

 * Services and infrastructure should not be tested in code tests
 * Code should be written to handle this sort of thing.
 * Hard to get away from. 
 * Example: Multiple servers
 
Continuous integration
=======================

 * Jenkins is your friend (http://jenkins-ci.org/)
 * Track code coverage
 
Worst Practice: Not testing
===========================

There're lots of things you can do wrong in testing
 
    * Not having them
    * Writing them badly
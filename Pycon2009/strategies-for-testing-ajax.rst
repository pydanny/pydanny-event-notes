======================
5 essential strategies
======================

Why?

    * Quickest way to verify that all features 'work'
    * Freedom to experiment
    * Manual testing is error prone and time-consuming
        - does not scale
        - people are lazy
        - Hard to test edge cases
        
Useful tools
==============

    - http://javascriptlint.com
        * Validate against multiple browsers
    - http://www.mozilla.org/rhino
        * no browser, command line
        * continuous integration
        * no DOM
    - Check out python spidermonkey C bindings
    - Browser tests
        * Selenium, Windmill
        * hard to automate
    - QUnit for JQuery
    - http://saucelabs.com/
    
    
   
Strategies
============   
        
    1. Test Data Handlers
    2. Test JavaScript
    3. Isolate UI for testing
    4. Automate UI tests
        - Continuous integration
        - Make it easy
    5. Gridify your tests
        - Generate reports
        - Selenium Grid
        - saucelabs.com
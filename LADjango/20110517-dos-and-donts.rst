=============================
Django testing dos and don'ts
=============================

**Note**: Example code was dark background with gloomy fonts that no one could read.

mahalow
90401902

The presentation
================

* Do: use AssertEquals/AssertNotEquals

    * Don't: AssertTrue is not good
    
* Do: Build TestCase Sub-classes

    * Don't repeat yourself
    
        * Create users
        * Create objects
        * Log users in
        * Clear cache
    
    * Don't make your reusable test methods not too complex
    
 * Do: Test all possible user cases
 
    * Analyze all possible exit points of a function
        * All returns
        * all expected exceptions
        
    * Shoot for 80% code coverage

 * Do: Test that data changes on success
 
    * Don't just asset that the function ran successfully
    * If data has changed, assert that the DB holds updated data
    * If cache was manipulated, assert that it is correct
    
 * Do: Use controls for complex testing
 
    * Create a control record/object to make sure complex functions don't touch unrelated elements.
    
    * Example: To check user deletion, create `user_to_be_deleted` and `control_user`
    
 * Do: Write **very** specific tests
 
    * in most cases, a given test function should be no more than 10-15 lines long (use your setUp function!)
    
 * Do: Test more than one type of use-case
 
    * Testing all error use-cases are as useful as testing for success
    
    * Success use-cases can still succeed, but for varying reasons over time.
    
 * Do: Keep your tests dirt simple. Don't write tests that require tests of their own
 
    * Don't: Write TestCase-specific Helper functions
 
 * Don't: Test everything in one big TestCase
 
    * Use many test cases: `test_managers`, `test_models`, `test_views`
    
 * Don't do these things
 
    * Write tests that go beyond your codebase
    * Use fixtures for everything
    * Write unnecessary code
    * Repeat yourself
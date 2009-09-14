=================================
Coverage Testing - good and bad
=================================

    * WRITE SOME CODE! (happy)
    * Does it work? (sad)
    
Coverage Measurement
=========================

    * Shows which lines of code are executing
    * How much of your code is covered by your tests?
    * Your tests test your product
    * Coverage testing **tests your tests**
    
Coverage tools
=================================

    * trace.py in standard library
    * figleaf by Dr. Titus Brown
    * coverage
    
Running coverage
-----------------

cli::

    $ coverage -e x test_mycode.py arg1 arg2
    $ coverage -r -m
    
Can also annotate source files.
Can run as a Nose plugin
can run it programmatically::

    import coverage
    coverage.blah()
    
Good side of things
------------------------

    * Statements are marked as executed or not
    * window into your code.
    * Fine tune by marking clauses to ignore via pragma
    * Clauses can be ignored by regex    
    * Write more tests
    
Bad: blunt tool
------------------

    * Everything considered important
    * Leads to many false alarms
    * Excluding code to boost coverage is too easy
        - Tempting
        - You'll never come back
        - You are only hurting yourself
    
Goals of coverage measurement
------------------------------------

    * 100% coverage 
        - ideal
        - Not always possible
        - real world issues are thorny. Hardware failures for example
    * Practical goals
        - more coverage is better
        - Actual number doesn't matter
        - False quantifiability: bad! Only cover what matters!
        - Use coverage results to understand your code.
        
100% coverage issue
------------------------

    - You can fool yourself into thinking you are bug free.
    - Tests can have bugs too!
    - Doesn't deal with path coverage
    
How coverage works
------------------

    * sys.stack_trace()
    * you can trick the trace function
    * Lie to python about where the lines are
    * Trace byte codes rater than statements
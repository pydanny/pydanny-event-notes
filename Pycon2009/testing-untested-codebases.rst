===================================
Testing large, untested code bases
===================================

Dr. C. Titus Brown

tools
--------

    * figlead


The code base
----------------

    * 8k of python, 2k of pyrex
    * Little app/UI code almost all library and framework
    * Grew of accretion and personal use at UCLA
    * Lots of technical debt
    
Issues with code base
------------------------

    * written at high level throughout
    * lots of unfamiliar code
    * functional
    * Mix of developers
    * Crosses domains
    * Performance is critical
    
What we already know
------------------------

    * Unit tests and functional tests rock: use 'em
    * Code coverage is of limited utility because it doesn't measure branch coverage
    * Code coverage is invaluable when aimed at:
        - new test efforts on legacy code
        - understanding code bases
        - legacy code is code that does not have systematic tests
        
        
Software forensics
---------------------

    * understanding big code bases is hard
    * Code coverage can be used as a lever:
        - "Give me but a place to stand and with a lever I will move the entire world"

Grokking code thru coverage
------------------------------

    1. Start with minimum useful statement
    2. Examine code that's actually executed
    3. Add additional statement
    4. Examine executed code
    5. Repeat
    

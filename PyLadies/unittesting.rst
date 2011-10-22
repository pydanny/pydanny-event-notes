===============
Unit Testing
===============

by Professor Ray Toal Loyala Marymount


How to unit test
==================

* Not manually
* You wrote code that exercises your code
* Perform assertions that record

    * That you get the results you expect
    
# TODO - get more info
    
Test Driven Development
=========================

#. Write some tests
#. Run them

    * They'll fail cause you have no code
    
#. Write some code
#. Now run the tests again
#. Work until the tests pass
#. Iterate!

Unit testing in Python
=========================

* Uses the module `unittest` is already there
* Docs

    * Python 2.7
    * Python 3 (http://python.readthedocs.org/en/latest/library/unittest.html)
    
First example
================

Interleave two lists::

    interleave([], [])
    interleave([1,2,3], [1,2,3,4,5])
    interleave([1,2,3], ["hello, world",])    

Test code:

.. sourcecode:: python

    # test_interleave.py
    from interleave import interleave
    import unittest
    
    class TestGettingStarted(unittest.TestCase):
        def test_interleave(self):
            cases = [
                ([],[],[]),
                ([1,2,3], [1,2,3,4,5]),
                ([1,2,3], ["hello, world",])
            ]
            for case in cases:
                self.assertEqual(interleave(case[0], case[1], case[2]))
            
    # interleave.py
    def interleave(a, b):
        # will fail. Fix
        return [x for x in izip_longest(a, b) for y in x if y is not None]
        
    
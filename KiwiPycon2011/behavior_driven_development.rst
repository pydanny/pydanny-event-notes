==============================
Behaviour Driven Development
==============================

By Malcolm Tredennick

* Slides at http://github.com/malcolmt/bdd-and-testing-talk

Why have I asked you here today
===============================

* Testing landscape
* A different way to think about this
* Code

Intro
===========

Data
----

* Stubs is empty data
* Mocking is pretend versions of data

Mocks
-----

* Substitute for external systems & components
* Need to be injected into the tests

    * "monkey patching"
    * Dependency injection

* Problem: Mocks need to be kept in synch with reality

.. warning:: I've run into this with mocks. This is why Open Comparison includes real API calls to it's target systems.

Testing Strategies
-------------------------

* formal verification
* test everything you can think of
* anti-regression suite

    * no bug fix without a test
    
* Test Driven Development (TDD)

    * Wraite failing test for next method or clas
    * Write minimal code to make test pass
    * Rinse, wash, repeat
    * Kind of drives Malolm crazy
    * Really about "*specification, not verification*"
    
* Documentation Driven Development (DDD)
* Behavior Driven Development (BDD)

BDD
====

Here we go!

Specification
---------------

* On paper
* Capturing the idea is probably good
* "What was I *thinking* when I cooked this up?"

.. parsed-literal::

    As a [user or role]
    I want [feature]
    so that [something happens]
    
BDD
-----

* What is the next most important thing the code should do?

    * Need to be able to test 
    * Need to be able to run
    
Scenario
--------

.. parsed-literal::

    Given that [initial context],
    if and when [some event occurs],
    then [ensure some outcomes]
    
Interlude: Naming things
-------------------------

* Language helps guide our brain
* Focuses the mind
* Perhaps too exclusively

**The Sapir-Whorf Hypothesis**

.. note:: Read http://en.wikipedia.org/wiki/Sapir-Whorf_Hypothesis

Test Titles
-----------

.. sourcecode:: python

    class BasicFieldTests(TestCase):
        def test_field_name(self):
            ...
        def test_show_hidden_fields(self):
            ...
            
Better:

.. sourcecode:: python

    class Fields(TestCase):
        def show_allow_name_override(self):
            ...
            
    class ChoiceFields(TestCase):
        def should_permit_initial_values_in_hidden_widgets(self):
            ...
            
Excercise
----------

 * write a `load_test` that changes the `test_` prefix with `should_` prefix
 * Cause language matters

Closing thoughts on unittest
-----------------------------

* Create more test classes
* Make them more explicit

DSL Packages for testing
-------------------------

* Lettuce (via PyPI)
* Freshen (via PyPI)

These tools are unique and probably good showing to non-coder types with money.

Conclusions
=============

* Behavioral tests are worth trying
* Question the way you think from time to time
* Are your tests' purpose clear to future you



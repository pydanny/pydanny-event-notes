==============================
Behaviour Driven Development
==============================

By Malcolm

Why have I asked you here today
===============================

* Testing landscape
* A different way to think about this
* Code

Some terms
===========

* Stubs is empty data
* Mocking is pretend versions of data

Mocks
======

* Substitute for external systems & components
* Need to be injected into the tests

    * "monkey patching"
    * Dependency injection

* Problem: Mocks need to be kept in synch with reality

.. warning:: I've run into this with mocks. This is why Open Comparison includes real API calls to it's target systems.

Testing Strategies
==================

* formal verification
* test everything you can think of
* anti-regression suite

    * no bug fix without a test
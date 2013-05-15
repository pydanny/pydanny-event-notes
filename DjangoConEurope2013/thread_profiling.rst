==============================
Thread Profiling in Python
==============================

by Amjith Ramamujam

    * Works for http://newrelic.com

This talk will give a tour of different profiling techniques available for Python applications. We'll cover specific modules in Python for doing function profiling and line level profiling. We'll show the short comings of such mechanisms in production and discuss how to do sampled profiling of specific functions. We'll finish with statistical profilers that use thread stack interrogation.

What's profiling?
==================

cProfile for profiling the performance of something

Usage::

    python -m CProfile sample.py


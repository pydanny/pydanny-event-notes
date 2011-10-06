=================
Embracing the GIL
=================

* by David Beazley
* slides: TODO

Embracing the GIL could be better
====================================

* People love to talk about it
* Rant about it
* Godwin's Law of Python?

premise
=======

* People love to hate on them
* That's because threads are useful
* Threads make great stuff work
* Even if you don't see them directly

The Gil in a Nutshell
=====================

 * Every Python file gets compiled into VM instructions
 * In cpython, it is unsafe to execute instruction concurrently
 * Hence: Locking

What GIL protects
====================

.. note:: duh missed this

Major GIL issues
====================

 * Threads using multiple CPUs
 * 
 
The Challenge
================
 
 * The GIL is unlikely to go away anytime soon
 * Can it be improved? Yes!
 * How can it be done?
 * How about Python 3!
 
Experiment
==========

 * request/reply server for size-prefixed messages
 * each method has payload/header
 
Why this experiment?
---------------------

 * Comes up in a lot of contexts
 * Involves IO
 * Used as a foundation for a lot of other things
 
Five different implementations
-----------------------------------

 * 1000 iterations of some simple code
 * Done on EC2 with nothing else running
 * implementations
 
    * C + 0mq
    * Python + 0mq
    * Python + multiprocessing
    * Python + blocking sockets
    * Python +  nonblocking sockets
    
 * Results
 
    * All finish in about 13 seconds    

What happens when you introduce a thread?
-------------------------------------------------

 * What does it do to the performance?

    * C + 0mq *(samish seed)*
    * Python + 0mq *(7x slower)*
    * Python + multiprocessing *(8.9x slower)*
    * Python + blocking sockets *(approx 10.x slower)*
    * Python +  nonblocking sockets *(approx 10.x slower)*

Commentary
-----------

 * Simple test
 * Not a hard-core realistic talk
 * How about PyPI?
 
    * What? Older version was 567 slower!
    * New version is much faster. .. note:: Get results!
    
.. warning:: Distracted by some work stuff. Missed some awesome stuff here.

Performance Explained - thread priorities
============================================

* To fix this, you need priorities
* The original "Fix GIL" patch had priorities
* That should be revisited

Another experiment
===================

* David's 3.2 fork with priorities
* Not suitable for real work
* Interesting for testing
* Lets you set the priorities manually

.. sourcecode:: python

    import sys
    import threading
    def my_function(value):
    
        sys.set_priority(-1) 
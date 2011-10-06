=================
Embracing the GIL
=================

by David Beazley

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
    * Python + multi
    * Python + blocking sockets
    * Python +  nonblocking sockets
    
 * Results
 
    * All finish in about 13 seconds    

What happens when you introduce a thread?
-------------------------------------------------

 * What does it do to the performance?



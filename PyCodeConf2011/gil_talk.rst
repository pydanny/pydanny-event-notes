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

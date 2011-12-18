===================
What is a callback?
===================

 * Its all about framework code that 'call back' into your code
 * Traditional code uses Hollywood principal, where "don't call us, we'll call you"
 * Callbacks are used for event-driven architectures (actual events, structuring of control flow)
 
Callback implementation
========================

 * Give someone a callable
 * Someone may store it somewhere

  - container, attribute, whatever
  - or keep as local variable

 * Calls when appropriate

  - When it needs some specific functionality (for customization)
  - Or when appropriate events occur (state changes, user actions, etc)
  
Customization
=============

 * Customizing sort (by key)
 
    * Read up on DSU pattern
    * Note that a little workaround is needed with the usual 'call a method on each object' OO idiom

.. sourcecode:: python  

    def DSU_sort(mylist, key):
        aux = [(key(v), j, v) for j,v in enumerate(mylist)]
        aux.sort()
        mylist[:] = [v for k, j, v in aux]
    
OO Customizing: the TM DP
=========================

Template method design patter: perform the callbacks by self delegation:
 
.. sourcecode:: python 
 
    class TMparent(object):
        self.somehook()
        
And customize by inheriting & overriding:

.. sourcecode:: python
 
    class TMchild(TMparent):
        pass

Customizing scheduling
======================

 * Sched needs TWO callback functionalities:
 
  - What time is it right now?
  - Wait (sleep) until time T
  
 * The OO way (more structured):
 
.. sourcecode:: python
 
    import time
    s=sched(time)
    
 * the FP way (more flexible):

.. sourcecode:: python
 
    s=sched(time.time,time.sleep)

 * You might supply callbacks or not 
 
 * (Dependency Injections DP & variants)

Events
======
 * Events proper
 
  - Observer/observable design pattern
  - GUI frameworks (mouse, keyboard)
  - asynchornous (event-driven) I/O 
  - System-event callbacks
  
 * Pseudo-events
 
  - parsing (SAX and other long tasks)
  - scheduled (sched)
  - concurrent (threads)
  - timing and debugging (timeit, pdb)
 
The Observer DP
===============

 * Target object lets you add observers
 * could be simple callables or objects
 * when the target's state changesm it calls back to the left observers know
 * Design choices:
 
  - General observers (callback on any state change)
  - Specific observers (callbacks on specific states)
  - grouped observers (objects with >1 methods for kinds of state-change) 
  
GUI frameworks
==============

 * Most classic of event-driven fields
 * consider Tkinter:
 
  - elementary callbacks for buttons 
  - flexible, advanced callbacks and events (pressing the 'a' button)
  - can also bind by class, all, root window, etc 
  
Callback issues
===============

 * What arguments are to be used on the call?
 
  - No arguments: simplest, a bit rough
  - In observer: pass as argument the target object whose state just changed
  
 * Or: a 'description of the state changes
 
  - Saves 'round trips' to obtain them
  
 * other: identifier or description of event
 * but?  WHAT?!?  check the PDF

Fixed args in callbacks
=======================

.. sourcecode:: python

    functools.partiabl(callable,*a,**kw)
        prebind any or all arguments
        x.setCbk(f,*a,**kw)
  
Callback dispatching
====================

 * What if more than one callback is set for a single event (or, observable target)?
 
  - Remember and call the latest one only
  - simplest, roughest
  
 * Remember and call them all
 
  - LIFO? FIFO?
  - How do you remove a callback?
  - Can one callback 'preempt' others
  
 * Can events (or state changes) be grouped?
 
  - use object w/methods instead of callable
  
Callback and Errors
===================

 * Are errors events like any others
 * Are they best singled-out?
 * Twisted Matrix's deferred pattern: look this up! It holds:
 
    * N chained callbacks for successes +
    * M chained callbacks for errors
    * each callback is held with opt `(*a, **kw)`

System-events callbacks
========================

 * For various Python system events:
 
.. sourcecode:: python
 
    atexit.register(callable, *a, **k)
    oldhandler = signal.signal(signum, callable)
    sys.displayhook, sys.excepthook, sys.setttrace(callable)
    
 * extension modules to that too:
 
  * readline.set_startup_hook
  * set_pre_input_ook
  * set_completer
  
Event-driven parsing
====================
 * SAX for XML
 
  - sometimes very big!
  - events are start and end of tags
  - handlers are responsible for keeping stack or other structure as needed
  - often not necessary to keep all
  
 * XML DOM on other side
 
Scheduled callbacks
===================

 * Standard library sched
 
.. sourcecode:: python 
 
    s = sched.Sched
    evt = s.enter(blah blah blah)
    s.run() #runs events 
 
Concurrent Callbacks
====================

 * Useful for SR check
 * threading.Thread(blah)
 * stacklet.tasklet (stackless python)
 * processing.Process( like threading.Thread)
 * NWS sleigh: eachElem, eachWorker
 
Timing and Debugging
====================

 * timeit.Timer(stmt, setup) 

  - string arguments to compile and execute
  - dynamic language twist on callbacl
  - event for callback

   - setup: once before anything else
   - stmt: many times for running
   
 * pdb module
 
  - pdb.run and .runeval: strings
  - pdb.runcall: callable, arguments
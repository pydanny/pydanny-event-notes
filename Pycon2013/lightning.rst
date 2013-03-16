================
Lightning Talks
================

.. note:: Live-noting lighting talks is very challenging. I'll do what I can but the level of detail provided in lightning talk notes will in general not be the same as my notes on normal talks.

Retask: Queue for humans (Kushal Das)
=======================================

* Simplest setup
* Ease of use
* redis backend
* https://pypi.python.org/pypi/retask
* retask.rtfd.org

.. code-block:: python

    # producer.py
    from retask.task import Task
    from retask.queue import Queue
    queue = Queue('example')
    info1 = {'user':'kushal', 'url':'http://kushaldas.in'}
    info2 = {'user':'fedora planet', 'url':'http://planet.fedoraproject.org'}
    task1 = Task(info1)
    task2 = Task(info2)
    queue.connect()
    queue.enqueue(task1)
    queue.enqueue(task2)

.. code-block:: python

    # consumer
    from retask.task import Task
    from retask.queue import Queue
    queue = Queue('example')
    queue.connect()
    while queue.length != 0:
        task = queue.dequeue()
        if task:
            print task.data
            
How and why a Java Expert switched to Python (Ron Cox)
========================================================

* Got into Java v1 ages ago
* Worked with servlets to deliver web sites
* About 2.5 years ago was working on mobile tech including Android and iOS work.
* Was tired of Java:

    * Java language wasn't productive enough.
    * Java platform was very resource intensive
    
* Tried Python for 2 weeks
    

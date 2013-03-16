================
Lightning Talks
================

.. note:: Live-noting lighting talks is very challenging. I'll do what I can but the level of detail provided in lightning talk notes will in general not be the same as my notes on normal talks.

.. warning:: If you are presenting, never, ever, ever, ever rely on the internet.

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
    
* New stack::

    Python 3.2
    CherryPy
    MongoDB
    Mailgun
    AWS
    
* Steve Holdren's comment: http://www.artima.com/weblogs/viewpost.jsp?thread=42242

Coding Across America (Matt Makai)
======================================

Coding Across America is a five month journey around the United States to learn and write about technology in thirty cities.

* 30 cities in 5 months
* Talk with developers from all cities
* Especially Python developers
* http://codingacrossamerica.com


Gitstreams (Justin Lily)
===========================

* Doesn't like the Github activity stream

    * Too much activity
    * Filtering isn't good enough
    
* gitstreams is an email digest of GitHub activity
* You choose the email frequency

NasberryPi (Mark Ransom)
============================

Home media server!

* Just started with RaspberryPi
* Got this working on a Pogo plug, should work fine with RaspberryPi
* What he has setup:

    * Fileserver
    * Media server
    * Web server (nginx, django) (For a personal home site, why does he use Nginx?)
    * Torrent server
    * More
    
* Setup is easy, just sudo apt-get 7 packages

European Conferences (Mike Mueller)
======================================

Euro SciPy
----------------

* August 21-24 in Brussels, Belgium
* 2 days of tutorials, 2 days of conference
* http://euroscipy.org

PyCon Germania
----------------

* Octover 14-19
* German speaking PyCon
* http://de.pycon.org

PyWeek Challenge (Richard Jones)
===================================

* Spend a week writing a video game using Python
* Learn more, create libraries, maybe even release something on Steam!
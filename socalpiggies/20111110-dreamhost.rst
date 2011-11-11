===============================================
June 6, 2011 - Socal Python meetup at Dreamhost
===============================================

.. note:: Arrived 30 minutes late so my notes are woefully incomplete

Asynchronous programming techniques
====================================

.. note:: My answer is to use Celery + Redis/RabbitMQ to handle most of this stuff

* Threads vs processes are a debatable issue.
* Cost of using Python to create new processes is considered slow
* Blocking and memory access issues
* Async is a problem in Python because not all libraries support it
* GIL

    * Multiple threads in Python are OS processes and you can get blocking on memory objects
    * On large processes on things like `dict` hash-tables you can get blocks/locks on the wrong thing
    
Multiprocessing
----------------

* Called 'giant hack'
* Looks likes the threads API
* Uses a messages system to use OS processes to share data between processes/threads
* Uses pickles to share data via messages, which means anything that is deserialized executes the code

    * Which means you should watch out for code injection!

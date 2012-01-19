=======================================
Diagnostics & Performance Computing
=======================================

by Dan Crosta, Software Engineer, 10gen

Speed
=====

* MongoDB is a high performance database
* But how do you know you are getting the best performance

Tools
=========

1. mongostat
-------------

* give it a host and port number. So we can connect to production. Woot!
* tons of useful columns 
* mapped
* vsize
* res
* faults - how many disk faults
* locked %

    * In a given window of time, measures two things (TODO find out)
    * Rough percentage measure - not perfectly accurate
        
2. serverStatus
----------------

What powers mongostat

.. sourcecode:: javascript

    > db.serverStatus();
        {
            "host":"MacBook.local",
            "version": "2.0.1",
            "prodess": "mongod",
            
        // lots more stats
        }
        
3. Profiler
------------

.. sourcecode:: javascript

    > db.setProfilingLevel(2)
        {"was": 0, "slowms": 100, "ok": 1}
        
This saves the data into a collection within the MongoDB. Which is nice cause you can reference it later.

See it in operation!

.. sourcecode:: javascript

    > db.system.profile.find()
        {
        "ts": ISODate,
        "op": "query",
        "ns": "docs.spreadsheet",
        "query": {"username":"dcrosta"},
        "scanned": 200001,
        "millis": 1407
        // tons more!
        }

.. note:: This is a capped collection of 1MB. So it stores only the most recent. You can change this with some hacks. TODO - find it out

4. Monitoring Service
-------------------------

* MMS: 10gen.com/try-mms (Free service provided by 10gen)
* Also check out Nagios
* Also check out Munis

Common problems
================

1. Slow Operations
------------------

.. note: Didn't get where this query is called. TODO Need to get info from Dan Costa.

Check the logs! From the shell::

    query docs.spreadsheets ntoreturn:100
    reslen:510436
    nscanned:19976 { username: "dcrosta"}
    nreturned:100 147ms
    
This means you need to index the username field
    
2. Replication Lag
------------------

Every time you do a read/write, it hits a capped collection called the oplog. Replication
lag refers to the time between when a read/write is called and when it is performed.

Example: If you have a very high write rate on the Primary, your secondaries can have trouble keeping up.

3. Resident Memory
--------------------

Always use 64-bit!

.. sourcecode:: javascript

    > db.serverStatus().mem
    {
        "bits"64, // need 64, not 32
        "" resident: 7151
        "virtual": ???
        "???": ??
    }

.. sourcecode:: javascript

    > db.stats()
    {
    // other things
    "avgObjSize": 5107.02342342, // capped at 16MB
    "dataSixe": 234424323423, // make sure this doesn't exceed your server space!
    // other things    
    }

Equation::

    indexSize + dataSize <= RAM
    
4. Page Faults
--------------------

.. sourcecode:: javascript

    > db.serverStatus().extra_info
    
    {
        "heap_usage_buytes": 2313132,
        "page_faults": 2381
    }
    
5. Write Lock Percentage
----------------------------------------

.. sourcecode:: javascript

    > db.serverStatus().global_lock
    
    {
        "totalTime": 23234234,
        "lockTime": 134646546,
        "ration": 0.002342342
    
    }
    
What to look for: ???

6. Reader and Writer Queues
----------------------------

.. sourcecode:: javascript

    > db.serverStatus().globallock
    {
        "blah": "blak=h"
    
    }

.. sourcecode::

    > db.currentOp()
    
What to look for: Things that are eating up tons of process. To stop it, run:

.. sourcecode::

    > db.killOp()

7. Background Flushing
------------------------

.. sourcecode:: javascript

    > db.serverStatus().backgroundFlushing
    
    {
        "flushes": 5634,
        "total_ms": 83556,
        "average_ms": 14.832342342,
        "last_ms": 4,
        "last_finished": ISODate
        // lots more
    }
    
In some case you should flush more frequently then MongoDB does by default
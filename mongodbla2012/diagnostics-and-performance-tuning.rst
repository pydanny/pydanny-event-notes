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

    db.setProfilingLevel(2)
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
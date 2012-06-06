=============================================
Implementing real time web apps with Django
=============================================

by Kristian Ollegaard

* Works at Divio
* Django since 0.96
* Danish, but lived in Zurich for 1.5 years
* http://kristian.io
* http://twitter.com/oellegaard

Why real time?
================

* Better user experience
* More options in front end
* Make the web feel like native apps
* Showing live data
* Collaboration is much easier

Finding the right tool
========================

* Criterias

    * Use websockets but has fallbacks
    * Good browser support including old IE
    * Should be usable from Python
    * Does not require extensive changes in frontend
    * As fast as it can be
    
The tools you want
===================

* Node.js
    
    * Built on Chrome's JavaScript runtime
    * Uses an event-driven non-blocking I/O model
    
* Socket.io

    * one interface for all transport methods (sockets, polling, etc)
    * Compatible with almost everything
    
Why not implement it in Python?
===================================

* Already active community
* Can be used from python without too much trouble
* Most people know very basic javascript
* More importantly, frontend engineers know javascript and can therefore contribute to the different browser-specific implementations.

Using redis for cross-language communications
=================================================

* Support for many datatypes
* Can be used both as storage and as a queue
* Implemented in many different languages
* For the usage in this talk, any other queue could have been used as well

Basic Concept
==============

* Something happens, the user must be notified in real time

    * From Django we insert the new value into the queue
    * Node.js listens on the queue
    
.. code-block:: javascript

    var io = require('socket.io).listen(8001);
    var redis = require('redis').createClient();
    redis.psubscribe("socketio_*");
    
    // TODO add the rest
    
.. code-block:: html

    <!-- Add this part -->
    
.. code-block:: python

    import redis
    import json
    redis_subscribe = '???'  # TODO - finish this out
    
Hosting socket.io
===================

* Nginx does not support websockets!
* Needs its own app, if hosted on an application cloud (e.g. Heroku)
* Recommended to expose the node server directly

    * But hey, it's node.js, it scales!
    
Using this today?
==================

* Maybe not
* Do some research

Client Authentication
=======================

* Socket.io handles authentication from node -> client
* Currently no authentication between django and node
* Could possibly be solved by storing your sessions in redis and checking them between systems
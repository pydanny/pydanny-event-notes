===============
Lightning Talks
===============

Crowdsourcing from NZ
=====================

by Ben Healey

* Rant about Amazon US not allowing the outside world to participate because of terrorists
* Then talked about various services like http://crowdflower.com/ 

Web Socket
==========

by Alexander Abushkevich

* Provides mechanism for bi-direction data exchange between server and clients
* Seems to more practice thabn XmlHTTPRequests for long polling
* many python libraries

.. note:: I think Zed Shaw has ranted about web sockets. Need to ask him.

.. sourcecode:: javascript

    window.onload(){
        // TODO is this how this really works?
        var s = WebSocket('http://blarg.service.org/service')
        s.do_action
    
    }

Google App Engine
=================

by Greg Fawcett

* Google will be charging for it soon
* old version from Django
* Lots of frameworks ported there: `Web2py`, `Zope`, old versions of `Pyramid`
* Sends out inbound and outbound email
* NoSQL database BigTable
* Runs with a Google version of memcached. Question: How do you ask for it?
* Has scheduled task system
===============
Lightning Talks
===============

Web Scraping
=============

by Chris Esther

* http://pypi.python.org/pypi/selenium
* http://pypi.python.org/pypi/mechanize

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
* Google App Engine apparently ran the Royal Wedding website

Wiki-to-speech Robot Presentations
==================================

by John Graves

* Converts presenters notes to speech
* This way it will convert your slide shows to full presentations

Pythonic Slide Generation
==================================

by Leon Mathews

* Wrote some restructured text
* Using rst2pdf to generate slides 
* Created a slides.style file to define the results better
* Generated PDF slides

.. note:: TODO - ask him to provide source code and instructions

Valgrind Memcheck
=================

by Tim Penhey

* "*Humans are bad at finding memory leaks*"
* Not really a python talk, but rather a review of how to check for memory leaks.
* Created an alias to run his valgrind check with all the arguments already defined


Sorry state of the New Zealand Job Market
=========================================

by Juergen Brendel

* At NZ bookstore only could find 1 book on Python and one Django 0.96 books
* Need more Python jobs
* Need to expand the community

What Parkour Taught Me About Programming
=========================================

by Danver Braganza


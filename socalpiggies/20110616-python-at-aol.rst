======================================
June 6, 2011 - Python at AOL
======================================

.. note:: Late because of traffic so missed part of the first talk. Some of the audience commentary was not as polite as it should be, and I'm guilty of a little of it. However, in conversing with other attendees and especially potential speakers, it was determined that as a group we need to be better at handling speakers.

By Jathan (Security Engineer)

* Most of AOL is Java and Perl, and there remains a lot of TCL.
* A third of AOL staff are developers.
* Moving towards open source more and more!
* But they had 7 people at PyCon 2011.
* Still have 70% of the old infrastructure run by 25K employees now maintained by 4K employees
* Data centers in:

    * Dullas, Virginia
    * Manassas, Virginia
    * Mountain View, California
    * Somewhere in Germany

about.me
---------

A custom profile & personal analytics dashboard. Serves as a landing page for all your social sites.

* 100% Python

    * TurboGears
    * Celery
    * SQLAlchemy
    * CouchDB (entire backend?)


* Presented at PyCon 2011

    * Luke Gotzling (lead engineer)
    * http://bit.ly/aboutme_pycon2011
    
StudioNow
----------

* Create, manage, and syndicate online video

    * aquired by APOL in 2010
    * AOL's content farm
    * Seen eHow.com? Yeah, like that.

* Web Services

    * Django
    * Gunicorn + Gevent

* Video Transcoding (ffmpeg)

    * Celery
    * Fabric
    * Boto (EC2 interface)

Relegence
----------

"A major part of the AOL content infrastructure"

* Topical, Real-Time News

    * Aquired by AOL in 2006
    * Subscription-based service
    * Like lingospot.com
    * Used by most of AOL web properties.
    
* Topics API


    * All Django all the time

AOL Mail - Anti-Spam Operations
--------------------------------

* Protecting AOL users from spam
* Whitelisting the Internet
* Tons of CLI Tools!
* Django Web Services

    * Anti-Abuse API
    * Mail Reputation Service

AOL Networking Engineering - Networking Security
--------------------------------------------------

What Jathan does for work.

* Protecting AOL from becoming Sony
* Blacklisting the Internet!
* Firewall Policy Management

    * 4 data centers
    * 850K+ policy lines
    * 37000+ host nodes
    * 5,300 host nodes

* Simian Python suite of tools:

    * Twisted
    * Django
    * SimpleParse
    * Suds

        * A SOAP library for Python

    * Netaddr
    * Nudge (Evite's API library)
    
        * Not selling this product so they don't need to worry about the GPL on Nudge.    

History of Getting Python into AOL
------------------------------------------

* Moved to Python from Perl in 2006.
* Had to deal with thousands of moving components and twisted solved a major problem.
* Entire network/security system is in Python.
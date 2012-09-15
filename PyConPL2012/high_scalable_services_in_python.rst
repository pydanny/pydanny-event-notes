==================================
Highly scalable services in Python
==================================

Original title: `Wysoko skalowalne serwisy pythonowe w OnetPoczcie`

* by Igor Waligóra

    * From Warsaw
    * Works on high integrity systems at Onet (https://twitter.com/onetpl)

.. note:: I'm translating this entire talk from Polish.
    I don't speak Polish except how to say, "Thanks" and "Questions?".


Talk Description (In Polish)
============================

W prezentacji pokażemy nasz model rozproszenia usług pocztowych, jak zrobiliśmy to przy użyciu Pythona. Pokażemy metody realizacji stabilnych i skalowalnych systemów utylizujących niskopoziomowe biblioteki oraz model ich zwielokrotnienia i integracji. Uchylimy rąbek tajemnicy działania jednego z największych systemów pocztowych w polskim Internecie.

System Architecture
====================

Some sort of email system

* 200 servers
* 20 database servers
* 1 Petabyte of data
* 4.7 million users
* 80 thousand requests a minute
* Spam

Server types
--------------

* SMTP

    * Postfix > MDA > Storage

* POP3 / IMAP

    * Dovecot > storage
    
* Webmail

    * PHP / JavaScript > Python Server > Storage
    

Persistence Server
-------------------

* check RFC 822

Their Python server
--------------------

* Tornado
* JSON-RPC

libOP - API
-------------

* libAUTH
* libDB
* libOCACHE
* libANTYSPAM
* libStorage

Making Python faster
=======================

Write in C, make bindings in Cython, import into Python

.. code-block:: c

    // op.c
    int mparser_fetch(const struct mparser_server *mparser, etc){
        [...]
    }
    
Workflow:

* Take C code that does what they need.
* Implement as Cython

    * http://cython.org

* Call the Cython modules from Python
* Put all the dependencies for the C library, Cython components, and Python into setup.py files so they can easily deploy

System Summary
----------------

* C
* Cython
* Tornado
* Python

Benefits
==========

* Challenging but successful implementation
* Good performance
* optimized to handle any load

    * 20x speed over standard Python

Critical tools
==================

* PyPI
* Virtualenv

.. code-block:: bash

    $ dpkg -i libop_1.1.0_amd64.deb
    $ mkvirtualenv mparser
    (mparser) $ source mparser/bin/activate
    $ pip install -r requirements.txt
    
Results
===================

* really good performance
* 99.8% uptime
* Able to handle 500 thousand spam hits a minute

Summary
============

* Build good systems
* C libraries are the way to go
* Use Python to build your stuff, but leverage in the C libraries
* Processes

    * Scrum
    * DevOps
    
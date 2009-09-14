======================
Internet Programming
======================

 * Wesley Chun
 * Author of Core Python Programming
 * http://starship.python.net/crew/wesc/cpp/
 
----
 
Sockets
=========

 
Client-Server architecture
--------------------------

Diagram::

    One-time request <--> Server <--> Clients
    
Servers un in an infinite loop

    1. Wait for client connection
    2. serve the request
    3. wait for client connection
    4. loop back
    
Definitions
------------

    * def: static execultable files are programs
    * def: Programs in execution are processes
    * sockets are the communicating mechanism 
    * Types:
        - Files
        - internet (AF_INET)

Socket Characteristics
------------------------
Two types

    1. Conenction oriented
        - stream based (SOCK_STREAM)
        - reliable and ordered
        - Transmission Control protocol (TCP)
        - Think like telephone conversation protocol
    2. Connectionless
        - Message/Datagram based (SOCK_DGRAM)
        - Unreliable and not necessarily ordered messages
        - User Datagram protocol (UDP)
        - Thing like postal service delivery protocol
        
Some things to consider        
        
    * Underlying Infrastructure IPC mechanism combinations
        - SOCK_STREAM + AF_INET (TCP/IP)
        - SOCK_DGRAM + AF_INET (UDP/IP)
        - Can also use both with AF_UNIX/AF_LOCAL
        
Connection-Oriented Call Sequence
----------------------------------------

Server side:

    1. Create a socket
    2. Bind to the socket
    3. start listening to the connection
    4. Infinite loop so when a client does connect that fires off a process that communicates back to them.
    
Client side:

    1. Create a socket
    2. Connect to a server via the socket
    3. Send a request to the server
    4. Handle the response
    5. Finish and close
    
Connectionless Call Sequence
--------------------------------

Server:

    1. Create a socket
    2. Bind to the socket
    3. receive and send
    4. close
    
Client:

    1. Create a socket
    2. Make a request
    3. Close

SOCKET MODULE
----------------
the module::

    socket() - creates socket object
    SOCK_STREAM - flag to set up TCP
    SOCK_DGRAM - flag to set up UDP
    AF_INET - Flag to set up an internet socket
    AF_UNIX - Flag to set up a Unix socket

SocketServer Module
---------------------

    * Simplifies all that we have seen
        - Provide socket server boilerplate code
        - Types provided: TCP & UDP for UNix and stuff
        - request Handlers
        
    * How to use socket Server
        - Much simpler
        - Create a request handling class with method
        - Create a socket server given the address and pass it to your handler class
        - Enter server's infinite loop
        
    * Base request handlers require socket-like access
    * Stream and Datagram RF's provide more file-like access
    * Setting up a UDP server is similar
    
Asynchronous Server
---------------------

    * Use UDP: this is poor man' asynchronicity
    * asyncore provides asynchronous service by using **select** and manage clients via an event loop
    * SocketServer has true ansync behavior
        - multiple threads (THreading)
        - Multiple processes (Forking)
        - same applies to Unix family sockets
        
----

=============================
Internet Client Programming
=============================

Various protocols

    * File Transfer Protol (FTP)
    * NNTP (News to news protocol)
    * Post office Protocol (POP3)
    * HTTP


File transferring protocols
=============================

    * FTP
    * UUCP (uncommon)
    * HTTP (primarily download)
    * SCP
    
ftplib module
----------------

    * ftplib.FTP class is all you need:
        - login()
        - quit()
        - more
        
code::

    from ftplib import FTP
    f = FTP('ftp.mozilla.org)
    f.login('anonymous', 'guess@who.org')
    f.dir()
    f.quit()
    
Some gotchas:

    * Primitive once you connect
    
----
    
Network News Transfer Protocol
===============================

    * NNTP
    * News archived for a certain  period of time
    * Login/password not necessarily required
    * Server may or may not allow 'posting' of messages
    * Not all newsgroups may be archived on a server.
    
nntp module
--------------

 * only need to import nntplib.NNTP
 
code::

    from nntp import NNTP
    n = NNTP('my.news.server')
    r,c,f,l,g = n.group('comp.lang.python')
    ...
    n.quit()
    
----

Electronic Mail Transferring Protocols
==========================================

    * Message Transport Agent (MTA)
    * Message Transport System (MTS)
    * Message User Agent (MUA)
    
Post Office Protocol version 3 (POP3)
---------------------------------------

    * Email used to be delivered to your system via SMTP
    * Resources/complexity made SMTP inefficient
        - Lack of recources
        - Expensive to keep/maintain
    * Users should be given local control of their mail
    
poplib module
---------------

    * Need to just import poplib.POP3
    
code::

    from poplib import POP3
    p = POP3('pop.mail.com')
    p.user('dgreenfe')
    ...
    p.pass_('youllNeverGUess')
    ...
    p.quit()
    
Simple Mail Transfer Protocol (SMTP)
----------------------------------------

    * Email "hops" from MTA-to-MTA via SMTP
    * continues until e-mail reaches final destination
    * Well-known SMTP servers include:
        - sendmail, exim, postfix, qmail
        - **commercial junk**: Novell, Sun, Microsoft
        
code:

    from smtplib import SMTP
    s = SMTP('smtp.hq.nasa.gov')
    ...
    sendmail(sender, recipe, msg)
    ...
    s.quit()

----
    
Other Protocol clients
=======================

    * telnetlib (telnet remote computer login)
    * gopherlib (is this still used anywhere?)
    
----

==================
CGI Programming
==================

    * CGI is neat and new!
    * CGI is the wave of the future
    * CGI is all about writing C!
    * Ha ha ha
 
Why does CGI suck?
--------------------

    * Not fast
    * Gets complex fast
    * Way too manual

2 line web server    
--------------------

code:

    from CGIHTTPServer import test
    test()
    
----
    
========
Django
========


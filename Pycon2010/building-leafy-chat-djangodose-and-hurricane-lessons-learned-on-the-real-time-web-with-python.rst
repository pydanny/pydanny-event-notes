Leafy Chat
==========

by Alex Gaynor

*TODO: Get the slides later*

Intro
------

Using AJAX, comet, and lessons learned

LeafyChat
---------

 * Used in Django Dash
 * Leah Culver, Chris Wainstroth
 * Orbited to handle proxying
 * Orbited for Comet
 * Twisted to handle IRC/Orbited connection
 * Used JSON as message packet format for **EVERYTHING**
 
Conclusiuons
~~~~~~~~~~~~

 * Kinda works
 
 * Messy
 
   * IRC in same process as comment so it doesn't scale
     
   * Any changes goes on the server, the client and the UI lib.
   
DjangoDose
----------

 * Built in a week before than DjangoCon
 
 * Built on twisted, orbited, Django, and StompMQ
 
 * Brian Rosner, Eric Florenzano
 
 * Instead of individual channels just one channel on a message queue.
 
 * Works really well for larger scale
 
 * Initial users had repeats of early data
 
Hurricane
---------

 * An attempt to take lessons learned from LeafyChat and DjangoDose and build a framework
 
 * Uses producers and consumers in a planned, managed method.
 
 * But done on no sleep over 40 hours - had abstraction issues
 
 * Tornado
 
 * Multiprocesses
 
Pycon 2010
----------

 * Do the same thing as Hurricane but better. Include a lot more data (flickr, github) and users (Pycon)
 
 * Uses redis
 
 * Orbited proxies to a twisted Daeon
 
 *  One backend process for each item (one for RSS, twitter, etc)
 
 * Don't reinvent Orbited. Its really good at what it does
 
Conclusions
~~~~~~~~~~~

 * Use orbited
 * Asynchronous programming is hard
 
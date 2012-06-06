=============================================
Implementing real time web apps with Django
=============================================

by Kristian Ollegaard

* Works at Divio
* Django since 0.96
* Danish, but lived in Zurich for 1.5 years

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
===============
Scrap the Web
===============

    * Asheesh Laroia
    * http://pycon09.asheesh.org/
 
Things to remember
===================
 
 * Scrapists are people who scrape web pages. 
 * Ignore terms of service at your on peril.
 * DO NOT BECOME AN EVIL COMMENT SPAMMER
 * Hidden form fields
 * make traps for automated web scrapers look for emails
 * If its on the web, you can scrape it
    - Now you have an API for everything 
 
Why scrape the web?
--------------------
 
 * You can maintain interoperation with unmaintained systems
 * "Rogue interoperability"
 
Three perspectives
---------------------

    * Be a maverick
    * Use the old standby XML tools
    * "Use the web tools against the web"
    

Choosing a parser
------------------

    * Performance
    * Ease-of-use
    
 
----

Some tools
===========

 * BeautifulSoup is old and not maintained anymore
 * html5lib 
    - builds BeautifulSoup objects
    - builds elementTrees
 * lxml provides XPath
 * mechanize (so much better than urllib2!)
 * pyquery
 * DOMForm is a python module for web scraping but it is not maintained
 * python-spidermonkey is a bridge between python and spidermonkey
    - lets you build a python engine that lets you run Javascript inside of Python!
 * Firefox via SeleniumRC. Really powerful. Downside is that instances of Selenium is not cheap.

Mechanize
-----------
    
    * You may need to turn off robots control 
        - mechanize.Browser().set_handle_robots(False)
    * See some other tricks
    * Handles hidden fields and cookies
    

HTTP Headers for urllib
------------------------

    * Need to support headers in stuff via urllib2
    * 2xx: Success
    * 3xx: Redirection
    * 4xx: Error
    * JavaScript behavior does not mirror Firefox
    * Image download behavior
    * Cookie behavior
    * Invalid HTML handling behavior
    * Not emulating web browsers can cause all kinds of fun and random things to happen

----

HTTP Methods
=============

    * GET is for requesting a page
    * POST is for submitting a form to a server
    * PUT is for uploading files in WebDav
    * BREW is because POST is trademarked by Post.
    
robots.txt
-----------

    * Check out http://www.robotstxt.org

Getting around IP address limits
================================

    * ssh -D to borrow the IP the machine you can log in to
    * ssh -D 1080 asheesh.org
        - Binds the 1080 port number to your local
        - Sets up a soft proxy redirect to fake out people wondering who you are

----
    
Handling CAPTCHA
=================

     * Sometimes people only have a limited set of images
     * Audio analysis
     * Use SeleniumRC to let you do the CAPTCHA for things.
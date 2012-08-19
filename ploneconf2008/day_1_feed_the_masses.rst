============================
Day 1 - Feed the Masses
============================

* Introducing Vice - Outbound syndication in Plone via the Zope Component Architecture

* by Paul Bugni
* Wednesday 8, 2008


Agenda
--------
    - Syndication
    - Vice History and Demonstration
    - Zope Component Architecture
    - Vice Integration
    

    
Syndication
------------
    - Providing other ways for your site to provide content besides the browser
    - Great for frequently updated data
    - Web feeds, rss, atom, etc
    - Allows aggregators to target your site/feeds
        - Net News Wire
        - Feedburner
        - Google reader
        
Prevailing syndication formats
------------------------------
    - RSS 2.0
    - Atom 1.0
    
Exposing the myth of RSS compatibility
------------------------------------------
    - There are 9 different and incompatible versions of RSS
    - FeedParser handles them all
    - RSS has always had many branches
    - Check out wikipedia for map of RSS branches
    
Atom
-------
    - Designed to be done via consensus.  No branches!
    - Atom has required fields
    - Atom is gaining momentum because its easy to work with
    
Plone Syndication
------------------
    - RSS 1.0 is the current view
    - PLIP #128 is there to support RSS
    - Uses Zope Adapters (via Five) to provide new views
    
VICE
-----
    - Sponsored by GSOC
    - P4A multimedia support
    - Plone 3 only
    
Installing VICE
------------------
    - Add to the build.cfg
    
eggs = vice.plone.outbound
fake_zope_eggs = True    
    
Features
----------
    - Allows for recursion on objects, their children, and their children's children
    - By content type can select RSS, ATOM, or both
    - And even RSS 1.0
    - Can syndicate any container
    

Goals
------

    - Separation of concerns
    - easy to add new feed types
    - make it easy to add new attributes
    - Isolate complexity into manageable objects

----

    
I need to bring in my icky one for Chris cause that at least runs cool

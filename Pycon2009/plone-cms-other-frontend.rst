====================================
Plone front end other front end
====================================

 * Carlos A de la Guardia
 
Why Plone?
------------

     * all the great features
     * built on python
     
Problems with Plone
---------------------

    * Complex
    * Hard to extend
    * Can be slow
    * Plone does a lot of things
    * Forced to use caching
    * Caching is not always the answer to traffic
    * Sometimes we are asked to add a couple of features that are Plone-y
    * Easy to end up with Frankenplone
        - Becomes very hard to extend and maintain
        
Content Mirror
-----------------

    * Developed by Kapil
    * Serializes plone content into a relational database
    * Supports 3rd party / custom archetupes content
    * Simple to set up
    * completely automated
    * Works currently with 3.1
    * Configure the database via ZCML
    * Works with Oracle, PostGreSQL, and MySQL. I guess anything that SQLAlchemy 
    * easily extended
        - CouchDB anyone?
        - GAPE!
    
Now we can
------------

    * Use plone to manage content and manage workflow
    * Serve plone content fast

How does it work?
--------------------

    * Integrates into the Plone event stream
    * Uses SQLAlchemy to turn Plone schemas into tables
    * Each Plone content type gets its own table
    * Each custom content type gets its own table
    * Once set up, content changes are sent synchronously to the database
    
Several created front ends
----------------------------

    * Repoze.bfg
        - Lots of Zope styles
        - Much lighterthan-Zope infrastructure
    * Plango uses Django to generate Plone content
    

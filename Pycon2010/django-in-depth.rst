Django in Depth
===============

by James Bennet

*I was trying to fix some problems at work so my notes here are amazingly incomplete.*

Model Inheritence
-----------------

 * Abstract/concrete
 
   * ye aulde ``abstract = True``
   * Use cases: common field sets and/or methods and/or META declarations   
 
 * DB level
 
   * No special mechanism. Just subclass a model
   
   * You can't directly subclass
   
   * Always implemented as multi-table
   
   * Has OneToOne key to parent
   
   * Good for modeling the "is-a" relationship
   
   * I don't like it and neither does James Bennet
   
 * Python level inheritence
 
   * ``proxy = True``
   
   * Will use the parent's table
   
   * Must have one abstract parent
   
   * use cases: Adding methods to existing models, adding managers or changing Meta behavior
   
Django Views
------------

 * ``SystemExit`` is not caught by Django, otherwise can be caught
 
 * Exceptions raised by exception middleware or 404 pages
 
 * Deliberately uses empty ``Context`` because nothing about the ``Context`` can be trusted.
 
AdminSite
---------

Here we go!

Overriding templates
--------------------

 * 

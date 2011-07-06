==============================
Subtyping Pattern!
==============================

.. note:: In a recent design discussion with Nate Aune he said he thinks some of my common design patterns are really similiar to this approach. After striping away the Plone-isms, I have to say there is merit to what Nate thinks. (Danny 07/05/2011)

by Rocky Burt

What is subtyping?
===================

 -Allowing for the subtyping of an existing content type

Why subtyping?
===============

 -Many possible faces for existing content type
 -simple conversion
 -delayed specification
 -not exclusive to p4a.subtyper, just built off of it

use cases
===============-

 -Need diferent content identify depending on situation
 -ogg file is video or audio
 -transforming of identity based on event reaction
 -How do you handle when a file type is uploaded?

p4a.subtyper
===============

 -minimal framework
 -Hooks up subtypes into content menu
 -$easy_install p4a.subtyper
 -use workingenv or virtualenv or buildit as preferred
 -special subtype events
 
	 - add ISubtypAdded
	 - addISubtypeRemoved
	 
 -extension by adapters and schema's

demo
===============

 -new modules interfaces and IUlradoc

     -    IUltadoc os marker interface
     -    interface.alsoProvides(needs marker interface, IContentType)

 - create descripters module

  - new descripter class called UltraDocDescriptor
  
    - for_portal_type = when this content type is displayed, this descriptor will be provided
    
 - create ultraddoc.pt
 - register descriptor as utility
 - hook up new view applying to utility
 
  - lets you have different views all with files named differently

cases in Plone4Artists
==============================

 -Look at Audio, Video, Calendar
 
     - no mention of p4a.subtyper
     - But uses these techniques

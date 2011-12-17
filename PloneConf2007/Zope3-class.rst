============================================
Zope 3 for Plone Class Notes
============================================

_Zope 3 Training for Plone Developers: https://dev.serverzen.com/svn/public/documents/serverzen/training/zope3-for-plone-developers/docs/z3pd-training-preparation-notes.html

  - Primary focus is component architecture (CA).
  - Secondary focus is an application server.
  - Adds frameworks and apis built on the CA.
  - Five has been incrementally adding Z3 functionality for Z2.
  - Zope 3 DOES NOT deprecate archetypes
  - Complementary
  - Some area's overlap (schema's, form generation)


Exercise: Creating a functional test
============================================
  - Create a new Zope 2 product called Thoughtfulblog
  - Reed discovered that PloneTestCase only works in the Instance/Products directory, but you can semlink to it .


Gotcha
============================================
Can't mix and match Zope2.zpt and Zope3.zpt objects in Plone 2.5, but can do it in Plone 3.0.  So METAL is bad there.  This is why we should move to Plone 3.0.


Interfaces
============================================
  - Interfaces define what methods are there but doesn't define the logic inside.  It is an agreement of how to build a class and nothing else.  So any logic can be tacked on later.
  - zope.interface is a good solid way to do Python interfaces.  It can be used outside of Zope as seen in Twisted and other non-Zope projects.
  - Marker interfaces are interface classes that lack any attributes (methods, properties, etc).  A regular interface includes attributes.

Basic UI: View Components
============================================
  - A view component consists of a page template, python class, and some ZCML glue
  - Conventions places view components in a browser subpackage.
  - Views can be traversed to
  - Classes always take precedence
  - Five mapped a bunch of Zope 2 naming permissions to Zope 3.
    - Zope2.view is mapped to the standard Zope2 view system.
    - zcml: allowed_attributes is a list of properties that can be vieed with same permissions


Writing your own permissions
============================================
  - Use Products/Five/permissions.zcml as example
  - id is name of Zope2 permission
  - title must match string in CMF Permissions
  - Rocky admitted it was a crude system


Integrating Archetypes
============================================
Archetypes based classes are very good


Setting up the view
============================================
  - Views can be treated like regular CMF skin items
  - Views can be registed as content actions


Python scripts inside of templates
============================================
  - Just say no
  - Only return items that the pages really need.
  - Example inside a browser.py file: return [{'title': x.Title(), 'link': x.absolute_url()} for x in self.context.posts()]


Testing
=============================================
  - Look at ThoughtfulBlog/tests.py
  - And the relevant browser.txt and content.txt file
  - Awesome stuff


Sub-Type Pattern Syllabus
=============================================
  - Setting up the interfaces
  - Modifying the view
  - Introducing adapters
  - Adapting folders
  - Adapting smart folders
  - Summary and Q & A
  - Used in Plone4Artists Calendar, Media, and other bits
  - Three new interfaces
    - IBlog
    - IBlogCapable
    - IBlogEnhanced

  - Mapped browser:page:blog.html to work for IBlogEnhanced by using the for=".interfaces.IBlogEnhanced"
  - Difference between implements and provides, which is critical semantics
    - A class implements
    - An object provides

Adapters
=======================
  - A bridge from one type of object to another type
  - Say "no" to monkey patches
  - Say "yes" to adapters
  - Subclassing and aadapting are not exclusive
  - Done via ZCML (<adapter />) or ZCML plus python
  - Example:
  
    - ICare extends IVehicle
    - ITransport could be an adapter for getting mileage info for IVehicle

  - Excercise:
  
    - Create new atct module - This is atct.py
    - Create new class called ATCTFolderBlog
    - Implement new posts method which calls context.contentValues() and returns BlogPost instances
    - Wire up the adapter in configure.zcml


Revisiting Adapters
=======================
  - zope.app.annotation
  
    - Akin to property sheets
    - A way to mark unrelated metadata onto an existing object
    - Reusable method of reusing dictionary objects

  - Multi adapting takes more than one object to adapt
  - Sometimes it takes two object to make a bridge
  - example:
  
    - from zope import component
    - adapted = component.getAdapter(myfolder,provides=IBlog) # -or- 
    - adapted = IBLog(myfolder)# -or maybe?- 
    - adapted  cmoponent.getMultiAdapter((somelang, myfolder), provides=IBlog)

  - Views are multi-adapters
  
    - Adapts the context and request
    - Most often used as callables
    - getMultiAdapter((context,request),Interface,name=u'blog.html')


Utilities
========================
  - Global Utilities
  
    - Most common
    - Akin to typical python module lookup
    - can be overriden
    
  - How to lookup a utility
  
    - getUtility(ISomeInterface) #-or-
    
  - Exercise: Creating a global utility
  - Local Components
  
    - Defined at the site level
    - Zope 3 'site' is mostly noted by the presence of the ISite interface.
    - Most folderish objects can become Zope 3 ISites
    - A site is just a place to store the "component registry" 
    - Example: A blog share might have a site for 'news blogs' with news components and another site for 'food blogs' for food specific components.
    
  - Sites can be nested
  - All components can be overriden with the closest component registry
  - utilities are commonly overrideen.
  - Cannot be registered via ZCML, must be done in install module
  - Exercise: Make our global utility a local one
  - blocking somerthing from loading in Plone 3: zcml:condition="not installed Plone.app.portlets"
  - Tools to util
  - CMF tools are being deprecated in favor of utilities
  - CMF tools use getToolByName
  - Local utilities similiar to CMF tools
  - Interface + name is important, not just name
  - CMF tools being deprecated in favor utilities
  - Sources
  - Vocabularies (similiar type of source), similiar to Archetypes DisplayList
  - Vocabularies are frown upon when seperation of concerns is important
  - Standard 'source' ensures the 'view' of an item is calculated at request time (good time to figure out i18n)
  
    - ISource requires only that the 'in' operator works
    - Iterable sources (very common) require __iter__ and __len__
    - Source binders are another utility used to generate a source based on context
    - Excercise:
    
  -Permissions
  
    - Permissions are actually utilities providing IPermission
    - Permission objects have id, title, and description attributes
    - No longer 'just strings' in Zope 2
    - Example: Getting all the permissions via zopectl debug
    - >>> p =  zope.security.interfaces.IPermission
    - >>> p
    - <InterfaceClass zope.security.interfaces.IPermission>
    - >>> from zope import component
    - >>> component.getUtilitiesFor(p)  
    - <generator object at 0x25ab9e0>
    - >>> [x for x in  component.getUtilitiesFor(p)]

  - Custom Events
  
    - Common way to get notification when 'something; happens	
    - one component fires an even
    - zope.event.notify(evt)
    - one component 'subscribes to the event
    - Most common use of events
    - Registered callables (often functions)
    - Does it's work because an event was fired

  - Object events
    - Set of events provided and fire by core Zope
    - Examples are IObjectCreated and IObjectMoved
    - Used throughout Zope 3 and should be manually fired when necessary
    - manage_afterAdd is not good and is replaced via events
    - Since Zope 2.9, ObjectManager fires events properly
    - Object-Manager container manage_XXX methods deprecated in favor of listening for object events
    - Handy events::
    
      + IOBjectWillBeAddedEvent	
      + IOBjectAddedEvent
      + IOBjectWillBeRemovedEvent
      + IOBjectRemovedEvent
      
  - Current Archetypes base_edit fires object modified events
  - Plone 3 provides richer set of object events being fired


Advanced UI
========================
  - Zope 3 schemas
    - Simply an interface with more detailed attribute information
    - uses fields as described by zope.schema
    - Provides no UI specific information
    - Fields provided for all Python primitives (Int, TextLine, List, etc)
    - Fields provided for higher-level types (passwords, URI, DottedName, etc)
    - Text field type is for hold a string with many lines
    - TextLine is for holding a string with just one line


Forms & Widgets  
========================
  - Widgets are essentially views on schema field instances
    - Widgets provide IDisplayWidget or IInputWidget
    - Widgets must be callable
    - Widgets typically return HTML
    - getMultiAdapter((field,request),IInputWidget)
    - Automatic form generation via zope.formlib and Products.Five.formlib
    - forms are browser views which extend base classes provided by Products.Five.formlib
    - Edit forms can automatically popular form with current data (similiar to base_edit)


plone.app.form (part of Plone 3)
================================================
  - makes formlib generated forms more Plone-llike
  - provides extra widgets
  - useful with Plone 2.5 and moreso in Plone 3


Useful components
========================
  - Python properties rock
  - p4a.subtyper might be worth looking into
  - CMFonFive
    - Can be used to design menu items in Zope 3 style that will work for CMF
    - Interesting Stuff:
    
      - <browser:menuItem /> is how you do it

  - workingenv.py
  - zc.buildout
    - svn.plone.org/svn/ploneout/trunk
    
  - zope.app.intid
    - provides unique integer based id's for objects
    - fast lookup, uses btree's
    - alternative to UID lookups with the reference catalog
    - five.initid brings support to Zope 2 /Plone
    - Go find the bloddy readme
    
  - zope.cachedescriptors
    - cache descriptors cache their data upon first invocation
    - lazy propeties overwrite themselves with actual non-descriptor attributes

  - lovely.tag
    - Provides a fast tagging engine
    - Uses zope.app.initid to manage id mappings
    - can generate tag clouds, etc
    - http://Plone.tv has this as an example


Things to look at
========================

  - Plone4Artists
  
    - Uses sub typinng
    - Interesting stuff:
    
      - Enables both file and Blobfile
      - Uses Interfaces
      
        - IAudio
        - IPossibleAudo
        - IAudioEnhanced

  - Plone4ArtistsAudio
  - Interesting stuff:
  
    - Keeps Zope 3 products seperate from Zope 2 stuff


Formlib issues
========================
  - No calendar widget
  - No reference widget
  - No wysiwig rich text widget


Tangent: Plone 3
========================
  - Look up Plone 3 configlets
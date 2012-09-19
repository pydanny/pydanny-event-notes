==================================
Day 3 - Buildout by Clayton Parker
==================================

- Buildout

    - parts
    - recipes
    - command-line
    
- ZopeSkel

    - Custom recipes
    
Why buildout?
--------------

- because it rocks
- lets us fetch all the dependencies easily
- no more ugly checklists
- lets us put everything involved in setup into one configuration file
    
------    
    
Syntax
--------

- Variable substitution 

    - ``${part:option}``
    
- option additional and removal

    options = foo bar
    options += foo
    options -= bar
    
- Reserved characters

    - :$%{}
    - Don't use those things
    
- http-address: 11001 
- zeo-address: 10001
    
----
    

Parts and Recipes
--------------------

- Can't have a part without a recip
- Part is identified in brackets:

    - [plone]
    
Buildout
--------

Some notes about buildout::
    
    [buildout]
        eggs-directory = where to put eggs
        download directory = where to oput downloads
        zope directory = where zope should go 
        index = http://download.zope.org/ppix (for PYPI mirrors)
        
    [instance]
        event-log-level = debug
        
Recipes
--------

Find recipes on...

    - PYPI
    - collective
    
Plone recipes

    - plone.recipe.plone
    - plone.recipe.zope2install
    - plone.recipe.zope2instance
    - plone.recipe.squid
    
plone.recipe.zope2install::

    [zope2]
    recipe = plone.recipe.zope2install
    url = ${plone:zope2-url}
    fake-zope-eggs = true
    additional-fake-eggs = ZODB3
    skip-fake-eggs = 
        zope.testing
        zope.component
        zope.i18n

----

Extending Configuration
--------------------------

- buildout.cfg
- profiles

    - base.cfg
    - development.cfg
    - debug.cfg (high debug settings)
    - qa.cfg (testing tools included)
    - prod.cfg (squid, varnish, etc)
        
how to extend::

    [buildout]
    # profile we want to use
    extend = profiles
    
PIL integration!!!
-------------------

doh::

    [buildout]
    parts =
        PILwoTK
        
    [PILwoTK]
    recipe = zc.recipe.egg
    find-links = http://download.zope.org.distribution

Handy tips
--------------

TODO: get all this stuff. Some handy stuff from this talk::

    [instance]
    environment-vars = 
        TZ America/New_York
        
    [debugging]
    parts =
        debug-products
        debug-products-svn
        ipzope
        zope
    eggs =
        plone.reload # real handy for development!!!
        Products.PDBDebugMode
        Products.DocFinderTab
        Products.Clouseau
        Products.PrintingMailHost # sends mailhost messages to console instead of to email!!!
    zcml = 
        plone.reload

Useful command line tools

    - [ipzope]
    
        - sets up ipython for Zope without the ugliness!!!  Find this full setup!
        - Lots of handy featurs
    
    - [zopepy]
    
        - Python prompt with all the Zope eggs in it but doesn't start up zope.
        - Great for command-line stuff without the weight
    
Versions.cfg

    - Helps us control versions of everything in one simple file.
    
collective.recipe.zope2cluster

    - Controls instances
    
----

Creating recipes
-------------------

``$ paster create -t recipe my.recipe.example``

Recipe really just consists of::

    class Recipe
        def __init__(sefl,buildout,name,options): pass
        def install(self): pass
        def update(self): pass
        def uninstall(self):pass # find conditions for things
        
Question
-----------

- Plone Deployment workshop (Indianapolis Nov 19-21)
- Creates a plone site in your Zope! #asked by me!!!

    - collective.recipe.plonesite

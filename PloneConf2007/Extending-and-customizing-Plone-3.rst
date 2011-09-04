========================================
Extending and customizing Plone 3
========================================

.. note:: I don't remember this talk at all, but I see from my notes instructions for both buildout and generic setup, two things that caused me a lot of grief during my Zope/Plone days. In retrospect, these are tools that employ *configuration over convention*, which probably explains my dislike. (Danny 07/05/2011)

by Martin Aspelli
==================== 

Plone core developer and author.

Agenda
==================== 

 - Love the buildout
 - Embrace the egg
 - Policy: Repeatable
 - Dependencies
 - GenericSetup
 - Tests
 - Visual customization
 - Through the web development sucks

Interesting stuff
==================== 

 - Plone 3 is built off smaller packages so easier to test and reuse
 - They want to nix through-the-web development cause it SUCKS
 - Tell SVN to ignore Eggs

Glossary terms
==================== 

 - Policy Product
 - A pattern whereby a project has a single product which upon installation, installs all dependencies and customizations in one step.


Buildout
==================== 

Sample:: 

    $ paster create -t plone3_buildout test
    $ python bootstrap.py

kewl stuff - start building Plone 3 this way instead of manually
http://plone.org/documentation/tutorial/buildout


Policy Product
==================== 

 - (((Read the tutorial on buildout!)))
 - (((Read onout setuptools (easy setup) handles versions with dependencies)))
 - Create a new egg::

    $ cd src
    $ paster create -t plone example.policy

  - Namespace is example, package is policy, Zope 2 product is True, Zip-safe is False

- Tell bouildout about products

  - Declare it as a development egg so buildoutdoesn;t go to cheese shop
  - edit things so its reconginized to Zope 2 and zcml
  - Edit buildout.cfg:
  
 .. sourcecode:: cfg

      eggs =
           elementtree
           example.policy
       develop =	
       	   src/example.policy
       [instance]
       zcml =
    	???
    	
- rerun buildout::
    
    $./bin/buildout -o (or do -N to not update the egg)
    
- Egg now ready
- zcml stuff

  - install dependencies:
  
    - `<include package="pone.browserlayer" />`


Generic Setup
=================

 - XML syntax - bleah
 - Extension profile bolts ont a base profile to amend or change configuration.  
 
    - This is the most useful kind for third party developers
    
 - edit configure.zcml
 
  - include GS namespace
  - add in generic setup tag
    
 - managed via portal_setup but portal_quickinstaller knows how to install them too::

    $ mkdir -p example.policy/example/policy/profiles/default

Installation tests
====================

 - Need to get boilerplate off presentation documentation
 - This sets up a Plone site for testing with our example
 - create test_setup.py which tests that we got basic setup right


Visual Customization
====================

 - Zope 3 resources are customized with the 'layer' ZCML
 - Visual components involved
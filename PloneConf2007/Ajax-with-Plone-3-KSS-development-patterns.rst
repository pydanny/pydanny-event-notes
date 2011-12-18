========================================================
Ajax with Plone 3 : KSS development Patterns
========================================================

by Godefroid Chappelle - Bubblenet
--------------------------------------------------------

.. Note:: KSS is a Python/JavaScript library that runs in Plone that uses CSS-style dialogues instead of JavaScript ones. It is something I hope the Plone community has abandoned. Stick with JQuery instead. (Danny 07/05/2011)

Overview
========================================================

  - Goals of KSS
  - Design
  - Development patterns
  - test patterns

Goals
========================================================

  - Business logic should be computed on the server
  
    - Javascript implementations are not standardized
    - Transaction differences because you are creating a fat client
    
  - Good integration with current development process
  - Ensure we keep accessibility
  - As few JS as possible
  - Business logic should be computer on the server!


Design
========================================================

  - Kinetic stylesheets
  - event binding

  - Generic client-side engine
  
    - same as HTML
    - HTML snippets manipulation

  - Simple server-side API
  
    - dom on the server
    - commands

  - Plugins
  
    - avoid dependency on JS libraries


Development Patterns
========================================================
Do it in HTML only first. That way you have complete accessibility and its cross browser

  - Client-side
  
    - bind events
    - css selectors
    - get Data from HTML
    - Value providers

  - Server-side
  
    - KSS views
    - z3 browser views
    - inherit from kss.core.KSSView
  
  - Command Sets
  
    - Queried by name (core, zope, plone)
    - Z3 subscribers and components

  - FireKiss
  
    - Demo
    - Debug mode is possible
    - kssproject.org/downloads/firekiss.xpi


Test Patterns
========================================================

  - Don't use Selenium unless you create JS plugin
  - Check commands in KSS response
  - Kss.core.KSSViewTestCaseMixin
  - Check HTML elements in manipulated page
  
    - Selected for events
    - Selected for targets

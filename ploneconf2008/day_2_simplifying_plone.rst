============================
Day 2 - Thursday 9 2008
============================


Simplifying Plone by Martin Aspelli
=============================================

    - With a chainsaw
    - How we can make Plone more approachable from a developer's point of view
    
Introduction
--------------
    - Last conference was no more monkey patches
    - current embarrassments
        - blog support
        - rich media
        - import/export sucks
        - Plone is hard to learn
        - skinning course
        
Thank you Lennart
--------------------
    - What zope did wrong
        - Zope 2 has inverse learning curve
        - Zope 3 has outverse learning curve
        - Five has an inverse/outverse learning curve
        - Plone 4 needs a lumpy learning curve
    - Developers expect things to be easy
    
Process for making improvements to Plone
--------------------------------------------
Flowchart showing the process

    1. Ask what are issues
    2. Categorize the issues
    3. Evaluate the issues
    4. Identify the particulars of the issues
    5. Chop out the old stuff that sucks
    
Guiding lights
---------------
    - Grok
    - Repoze
    - Pylons
    - TurboGears
    - Repoze.bfg
    - web.py
    
Plone 4
----------

    - Steps to learning should mirror how development should work
        1. install
        2. content & settings
        3. colors/logo
        4. etc
        5. integration comes last
        
Things that work well
-------------------------
    - Installation
    - content editing
    - collections (good but UI sucks)
    - workflow
    - ZODB
    - settings
    - content rules
    - HTML and CSS

Cliffs
----------
These are the things that take work when you figure them out the first time
    
    - Changing the logo
    - branding ("my designer gave me this")
    - Content types ("I want to capture this data")
    - Deployment
        - Import and export of data
        - ZODB level configurations
    - Adapters ?!?
    
Some themes
--------------
    - Think about the audience
    - Find the one true way
    - Remove the other ways
    - customization registry
    - embrace through the web
    - ...but allow filesystem round-trip for deployment and collaboration
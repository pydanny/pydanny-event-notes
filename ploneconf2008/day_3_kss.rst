==========================
Day 3 - KSS by Joel Burton
==========================

- Joel is not a JavaScript expert
    
Overview
----------

- Why KSS
- Client-side convenience
- Server-side power
- Quick reference guide
    
Challenges of JavaScript
------------------------

- Another language
- Browser incompatibilities
- Even when done correctly...

    - Do it again in Python
        
What is KSS?
------------
    - Kinetic Style Sheets
        - Power of JS, syntax of CSS
        - Allows you to declare behavior
        - Includes AJAX library

KSS sample 1
------------------
basic example::

    #logButton:click {  /* identifier & event */
        action-client: alert;   /* client action: alert */
        alert-message: 'clicked';  /* parameters for alert */
    }


KSS sample 2
------------
More complex example::

    #logButton:click {  /* identifier & event */
        evt-click-preventdefault: True; /* Don't do normal thing */
        action-client: replaceInnerHTML;   /* client action: alert */
        replaceInnerHTML-kssSelector: "#message"; /*  */
        replaceInnerHTML-html: "Clicked (via KSS)";  /* parameters for alert */
    }

Registering KSS
-----------------
    - portal_kss in zmi
    - storing just like css

Timeouts
---------
    - Makes it so you can in-line page auto updates!
        - Stock market changes
        - Chat system

events
--------
    - click
    - dblclick
    - load
    - mouse events
    - timeouts
    - blur, change, field things
    - TODO: look up text change!

coreset
----------
    - replaceInnerHTML
    - insertHTMLafter
    - addClass: add css class to html
    - removeClass
    - toggleClass
    - focus on a given node
    
zope set of commands
----------------------
    - refresh a viewlet
    - zope.refreshViewlet (...stuff...)
    
plone portlet functions!!!
----------------------------    
    - refreshPortlet
    - issuePortalMessage
    
Debugging KSS
----------------
    - Use Firebug!
        - turn on portal_javascript debugging
    - type in your scripts directly
    
Future of KSS
----------------
    - Other JS libraries
        - for people who want to tinker deeply
    - Possible non-JS backends?
        - Flash
        - Silverlight
    - http://plonebootcamps.com/resources
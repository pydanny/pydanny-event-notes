==============================================
Best Practices for Front-End Django Developers
==============================================

by Christine Cheung

 * One of the co-founders of Pyladies 
 * Works for Red Interactive Agency
 * Does front end development
 
    * Also does a lot of backend stuff
    * Quickly mastered CBVs so she has serious chops
 
 * @webdevgirl on http://twitter.com/webdevgirl
 * http://xtine.net
 
Presentation is important
============================

 * Polixh front-end is as important as the front end

    * It may "scale"
    
    * But bloated markup and JavaScript will slow things
    
 * The implementation really matters
 
Start Organized
================

 * Structure the templates
 * Template Tags should express presentation, not logic 
 
    * Presentation and iteration over data, NOT manipulation
 
.. note:: I wish people remembered this bullet about template tags and logic

Cascading Style Sheets
=========================

 * Define a style guide. **Write it down!!!**
 * Consistent Variable naming
 
    * Camel case
    * dashes
    * underscores
    
 * Keep your css files small. Combine it in deployments    
 
JavaScript
==========

 * Use a framework!
 * Pick one and stick to it:
 
    * JQuery
    * Don't mix in other things like Dojo
    * Avoid plug-in overkill. No more than 3-4
    
        * Reduce performance hits and code conflicts
        * Analyze if you can write your own
        
 * Namespace your Javascript
 
    * TODO - get sample code from Christine
    
 * DON'Ts:
 
.. sourcecode:: html

    <script type="javascript">
        document.write('foo'');
    </script>
    <a onclick="blarg();">Stuff</a>
    
 * Lots of JavaScript? Use backbone.js
 
Don't do HTML from scratch: Use html5boilerplate
========================================================

 * Comes with a layout via 960
 * JQuery
 * Modernizr

    * You can do wicked class tricks with this tool. Wow
    * Need to really look at the slides cause she did this better than the docs
    
Sass/Compass instead of CSS
============================

 * CSS Authoring Framework + Utilities

    * SASS - nested rules, variables, mixins
    * Image Spriting
    
All about the data
==================

 * Leverage the power of both the front and back end

    * Share the work between the front and back side of things
    * Generic Class Based Views for quick prototyping 
    
Define you datatypes
====================================

 * Make an API
 * Share the models between back and front end
 
Tests
======

 * CSSLint
 * JSLint
 
    * .. warning:: it will make you cry
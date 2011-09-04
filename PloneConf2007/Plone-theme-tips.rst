===================
5 Plone theme tips
===================

.. note:: Lost the name of the author but this has the distinction of being the first Plone (or Python) conference talk I ever got to see. (Danny 07/05/2011)

Tip 5 - Centered Design
=========================

Fixed width:

.. sourcecode:: css

    #visual-portal-wrapper {
    width: 980px;
    margin-left:auto;
    margin-right:auto;
    }

    - Liquid Design
    #visual-portal-wrapper {
    width: 980px;
    margin-left:20%;
    margin-right:20%;
    }


Tip 4 -  integration of IE
=============================

 - put all stuff in IEFixes.css
 - Write styles for IE7 first
 - Then hack your styles for other IE version
 - portal top is top part of Plone
 - For IE6 and lower hack:
 
.. sourcecode:: css 

    // Below is IE7 , Firefox, and Safari
    #portal-top {
        background: blue;
    }
    // below is IE6 version
    html #portal-top {
        background:red;
    }
    
 - easy to use
 - almost no chance of breakage


Tip 3 - Styles alterations
=============================

 - different sections styling
 - site root
 
  - news: blue
  - products:orange
  - events: yellow;
  - about:green
  
how:

.. sourcecode:: css

    body.section-news {
        background-color: blue;
    }
    body.section-products {
        background-color: orange;
    }
    
    // This is auto-written and any_custom_view could be working_group.pt
    body.template-any_custom_view {
        background-color: spotted duck;
    }
    // example
    body.template-working_group_view.pt {
        background-color: spotted duck;
    }
    
Tip 2 - Drop down menus
===========================

- Suckerfish for Plone 2.5.x

  - Accessible
  - valid CSS
  - Obvious and clean XHTML
  
- Plone Dropdowns is for Plone 3.x

  - webcouturier.dropdownmenu
  - Build it out in folder items and use a heirarchy
  - Autobuilds via Plone 3 into portal tabs
  - Uses INavtreeStrategy
  - Uses SitemapQueryBuilder()
  
    - Can change the depth of the navtree via sitemap properties


Tip 1 - Rounded Corners
===========================

 - Cornerstone of designer's minds
 - pure CSS solution
 
  - Initial nifty corners
  - Too ugly XHTML
  - No hooks in Plone
  - People don't like dealing with CSS if they have to change images
  
 - Images based solutions
 
  - Sliding doors - often used for rounding corners
  - Adam Kalsey technique
  
    - Plone has XHTML hooks in portlets for this
    - pretty simple css
    - Most of the cases use nested HTML elements
    - Fixed set of images for the corners
    
 - JS + CSS solution
 
  - The most flexible
  - Doesn't require nested elements in HTML
  - Does not require additional CSS
  - Potential Solutions
  
    - Nifty Corners Cube (Javascript Library
    
      - First doesn not work with borders and background images
      
    - JQuery corners
    
      - Requires jquery and does not work with Safari
      
    - CurvyCorners library (recommended)
    
      - Supports most modern browsers
      - Works with borders
      - Works with background images
      - Supports antialiased corners 
      - Cons:
      
      	- Some problems when background images are used and box has different colors
      	
	- Does not work well when used with multiple boxes
	
     - collective.roundedcorners
     
       - On presenter's laptop
       - Normal Plone Package/Product
       - Uses a mix of Javascript + CSS
       - Raw, and will be released hopefully soon

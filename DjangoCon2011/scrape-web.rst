==================
Scraping the Web
==================

by Katharine Jarmul

 * Co-Founder and VP of PyLadies
 * twitter.com/kjam
 
Content is what you need
===========================

 * You need to get content
 * good content exists all over the web
 * Scrape it!
 
lxml
=====

 * lxml.etree good for good formatted xml
 * fast for SOAP or other xml-formatted content
 
.. sourcecode:: python

    def parse_feed_titles(rss_feed):
       data = [] 
       dochtml = html.document_fromstring(rss_feed)
       for x in dochtml.cssselect('title'):
            data.append(x)
            
lxml: cssselect
================

Uses a JQuery style language to grab bts

.. sourcecode:: python

    article_title = html.cssselect('div#content h1.title)
    
cssselect
=========

 * Learn css to help you scrape
 * Various developer tools help to find stuff (firebug)
 
iterlinks
==========

 * Good for high link pages or finding related links

.. sourcecode:: python

    page_links = html.iterlinks
    
sourceline
============

 * tells you the line the element is on
 * Helps you determine distance of one element is from another

.. sourcecode:: python

    pos = element.sourceline 


find,findall
==============

 * Find the element you want
 * Grab only what you need
 * 

.. sourcecode:: python

    spans = element.findall('span')

nodes of content
==================

 * Elements have children
 * Elements have siblings 
 * Elements have ancestors
 
.. sourcecode:: python

    h1s = list(h1_element.itersiblings())
    the_kids = [c for c in element.iterchildren() if len(c.text)]
    
Web pages change
=================

 * All your code can break
 * Make a monitoring system to let you know it things change
 
    * Code that checks the pattern of the layout
 
forms
======

 * Think: log in pages
 * Don't use **lxml** for evil
 * See lxml docs on how to process them


text, text_content, iter_text
================================

.. sourcecode:: python 

    text = element.text
    text_w_content = element.text_content()
    text_bit_by_bit = list(element.itertext()) # The best way!

Tips for maintainable scrapers
================================

 * Skip ugly parsing
 * Text = Content = Boss

XPATH fundamentals
====================

 * Not fun but you need to learn it to handle XML. I hate it
 * lxml supports it, of course
 
Building LXML w/LXML
====================

 * Writing templates for things like xml are boring
 * **Don't be that guy/gal**

.. note:: Not showing the example because kjam says it is evil!


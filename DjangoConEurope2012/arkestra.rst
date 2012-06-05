================================================================
Arkestra: semantic information publishing for organizations
================================================================

by Daniele Procida

* Works at Cardiff University School of Medicine
* http://medicine.cf.ac.uk is his main site
* http://arkestra-project.org/
* http://readthedocs.org/docs/arkestra/

.. note:: Good talk but some slides had too many bullets. 

What typically happens when working with a CMS
==========================================================

* You have to repeat yourself
* data gets wasted and lost
* content & presentation becomes inconsistent
* info in templates gets broken and petrifies
* information ages, withers & dies
* users play fast & loose
* The larger the site the worse the problems get

His idea
=========

Create a model of the real world

Informtation, not just data
==============================

* information not useless stupid data
* templates don't hold information
* Semantic modeling  real-world relationships
* user semantics!

Organization
============

* Can you model a CMS based off an organization?
* He created a concept of ``entity``
* Many interconnections of content and data
* He did it on http://medicine.cf.ac.uk

    * Entities are associated with pages
    * Not entity needs to have a page

* We did a very similar effort on http://science.nasa.gov/, but...

    * not so well organized.
    * grown organically during the course of a number of badly run meetings
    
Don't waste people's time
=================================

* Make everything re-usable and re-use it
* Make it easier to re-use then re-enter

Django-CMS and Arkestra
=========================

* Django CMS & Arkestra grew up together
* have been developed alongside each other
* portions of Django CMS conceived as part of Arkestra
* integration with pages, placeholders/plugins, menus

The Semantic Presentation Editor
==================================

The problem:

* Create complex, flexible, multiple-column layouts
* produce well-structured semantic HTML
* Need no HTML/CSS skills

Solution:

* The Semantic Presentation Editor
* Special text editor that renders out things in a lovely, semantic fashion
# See https://bitbucket.org/spookylukey/semanticeditor/wiki/Home
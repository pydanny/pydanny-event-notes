=================================
Maintaining an old Django project
=================================

By Shawn Rider

.. contents:: Contents

Background
==========

PBS TeacherLine dates back to 2006. Catalogs, CMS, brochures, and classes lets
users added tons of content every year. Hundreds of classes and tens of thousands
of users.

Before 2006 TeacherLine was written in ColdFusion. Run on Windows, separated from the PBS architecture. PBS has a long history of development with open source. So a complete rebuild was necessary. Some technologies considered:

 * Ruby / Rails
 * PHP / Some PHP framework
 * Python / Django

What PBS likes about Django
============================

 * Speed of development
 * Code Quality
 * Modularity of framework
 * Django Admin
 * Active community
 * Python!
 
Things that worked for PBS
===========================

 * Django is opinionated in a generally good way
 * A culture of self-criticism
 * Isolate functionality into reusable components
 
Lessons learned
==================

 * Never override the User model
 * Make tests right away
 * Make the most of your VCS
 * use tests
 * take your time
 
Sell the upgrade to the Uppers
==============================

 * it will lower the cost of future development
 * it will alleviate a pain point felt by staff processes
 
What he wants
==============

 * Multi-configuration support out-of-the-box
 * A better way to know when Django's modules are completely loaded into memory
 * More robust handling (Signals++)
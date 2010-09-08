======================================
Why Django sucks and how we can fix it
======================================

By Eric Florenzano

.. contents:: Contents

Apps
====

Making custom changes to an app and now staying in trunk fails.
Apps that provide models are inherently inflexible.
primary key assumptions

Class based views to the rescue?
--------------------------------

 * No consensus on how to implement it?
 * Where do you put customized view subclasses?
 * urls.py is already overloaded

Generic Foreign Keys
====================

 * good for flexibility
 * Bad for configuration

Performance
===========

 * Things are slowing down
 * Memory usage is going up in each version since 1.0
 * performance is going down since 1.0
 
Django Core
============

 * Closed and very private
 * Why isn't Alex Gaynor not a core developer?
 * Why isn't there a truncatechars filter?
 
Badteries
=========

 * DataBrowse is a joke
 * lorem ipsum doesn't belong
 * Need to move to a DVCS

django.contrib.auth
-------------------

 * django.contrib.auth is inflexible
 * first_name, last_name is culturally limited
 * Admin is couple to user
 * Integer primary gey
 * get_profile is inelegant
 * no way to use secure key
 

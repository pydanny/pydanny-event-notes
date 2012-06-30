=======================
Maps of Imaginary Lands
=======================

* by Malcolm Tredinnick
* malcolmt
* https://github.com/malcolmt/imaginary-maps-in-django

The Goal
=========

* Build an imaginary land

The Problem
==============

* Not trivial
* Some preparation required
* May be new

    * THis should **not** be a problem, but... :-)
    
The Solution
================

* I have provided running code
* Github URL at end of the slides.

What is success?
================

* Get up to speed on Django and GeoDjango
* Run (and read) my code
* Do something better!

The Secret Tip
==============

* All maps are mashups

The Stack
===========

* PostGUS
* OpenLayer.js
* Mapnik
* Tilecache
* GeoDjango

OpenLayer.js
-------------

* Client side, Javascript framework
* For doing maps layering

Mapnik
-------------

* Server side way to combine data sources
* Different details and different zoom levels
* Input from raster or vector formats

Tilecache
-------------

* Caching tile
* Use this or mod_tile or tilestache or other
* Avoid recomputing common data

GeoDjango
-------------

* Use views to provide subset of data
* Easy default output in formats understood by OpenLayers

Imaginary Maps
===============

* Need to replace base image
* GeoAdmin needs to be customized for the imaginary maps
* Mapnik WMS server running locally

Sample Model Code
=================

.. code-block:: python

    class Track(models.Model):
        name = models.CharField(unique=True, max_length=50)
        path = models.LineStringField(geography=True)        
        objects = models.GeoManager()
        
        def __unicode__(self):
            return self.name

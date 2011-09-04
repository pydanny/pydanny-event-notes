===============
Treehugging
===============

by Brian Luft

Introduction
=============

Where do we find structured data:

    * Hierarchical data
    * graphs
    * organizations
    
Trees and relational database
-----------------------------

    * A table is not a tree. We need to do a few tricks

Adjacency List
~~~~~~~~~~~~~~

Self referential foreign key. This is how usually I've done it in the past.
Can be very cumbersome, requires a lot of joins, not obvious or easy.
My own note: I believe Oracle has a tool to deal with Adjacency Lists but its database specific

    * fast writes but slow reads
    * fragile update operations
    * You need to know what level in the tree your item is at when you look it up
    * Easy to create orphans by accident
    * Easy to start, hard to maintain
 
Nested sets
~~~~~~~~~~~

Not easy to set up and hard to modify. Query works reqardless of depth.

    * Efficient reads
    *  high maintenance cost
    
Materialized Paths
~~~~~~~~~~~~~~~~~~

Every node in the tree has a "path" attribute. I did this once.

    * Queries simple and fast
    * Effectively de normalized
    * Writes slow
    * Requires some wackiness when making adjustments
 
Django Apps
===========

    * django-mptt (we used this on http://science.nasa.gov/)
    * django-treebead

Comparison chart
 
 * http://www.qompr.com/charts/63;django-hierarchical-tree-data/
 
Versus:

 * Treebeard supports all three models, MPTT only handles Nest Sets
 * Both provide Move Node forms, MPTT provides a TreeNodeChoiceField(ModelChoiceField)
 * MPTT is being maintained, treebead has slightly more active development
 * Front end: Treebead has a get_annotated_list function, MPTT has some handy template tags / filters
 
Overall Impression:

 * Treebard: Overall impression: treebead model creation methods on model is weird and uncomfortable
 * MPTT: Related items methods
    
Miscellaneous
=============

    * django-treemenus - possibly solves some outstanding treebeard issues
    * neo4j - Designed for large graph systems but Java based
    * Suckerfish/Superfish - Some view related items
    * protovis
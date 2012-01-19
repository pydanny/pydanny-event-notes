==========================================
Schema Design
==========================================

by Kevin Hanson, Solutions Architect, 10gen

Parallels
==========

Tables == Collections
Row == Document
Column == Field
Index == Index
Join == Embedding & Linking
Schema Object == None

The Big Question
=================

Do we link or do we embed?

Embedded
---------

* Faster
* But large embeds can make the master document slow. Ex: If a document has a billion comments

Linked
--------

* Slower
* Returning the master document requires extra logic

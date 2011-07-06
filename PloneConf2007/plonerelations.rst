====================================
Relations with Alex Mitchell
====================================

.. note:: This tool lets you establish relationships between any two object types in Zope. The problem is that it is functionally duplicating with Zope/ZODB what relational databases give for free. (Danny 07/05/2011)

What is zc.relationship?
====================================

  - A low level ZODB index for querying relationships
  - Highly optimized for simple relationships across large data
  - Default confi allows relations between arbitrary persisten objects
  - index can be confired to index complex relationships including non-ZODB objects
  - provides transitive searches
  - con: hard to use in Plone

What is Plone.relations?
====================================

  - A local utility built on zc.relationship, which is application to a wide variety of relationship models
  - A relationship class that models many-to-many contentl relationships
  - Some options aspects of the relationship are also indexable

What is Plone.app.relations
====================================

  - higher level API
  - Content object for UML
  - A set of optional adapters and subscribers
  - DC workflow for relationships 
  - "Holding" relationships
  - Relationships which are copied when their source is copied.
  - example Plone code::

      src = IRelationshipSource(obj)
      src.createRelationship(target=obj)
      src.getTargets()

Relationship Source
=====================

  - IrelationshipSource
  
	- Create (createRelationship), supports multiple targets
	- Query (getTargets, isLInked, getRelationshipChains, getRelationships)
	- Modify (deleteRelationships)

Relationship Targets
=====================

  - IRelationshipTarget
  
    - Same query methods and parameters as IRelationshipSource + getSources
    - ISymmetricRelation
    
    -Query (isLinked, getRelationships, getRelations)

Code Samples
=====================

stuff from the presentation::

    >>> class IFriendship(IDCWorkflowableWorkship):
          """A friendship"""
    >>> source = IRelationshipSource(obj)
    >>> rel = source.createRelationships(obj, relation='friend', interfaces=(IFriendship)
    >>> list(source.getRelationships(relation='friend')
    <lazy list response>
    >>> list(rel.targets), list(rel.sources)
    >>> list(source.getTargets())
    >>> target.isLinked()

What can you do with it?
=========================

  - Model non-container relationships you might need
  
    - Social networking
    - User favorites
    - Placeless content
    - taxonomies or complex vocabularies


What has been done with it
==========================================

dailyreel.com
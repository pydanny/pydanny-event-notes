==========================
Reusable apps
==========================

By Alex Gaynor

Note: Alex talked FAST but it was one of the best talks at DjangoCon.

Basics

 * similiar patterns
 * write once, use everywhere
 * no need to reinvent this wheel

But Standard apps patterns are not truly reusable
=================================================

Too many differences in business logic between systems
 
 * ex comments:
   
  * comments apps have to cover many different business cases
     
  * differing storage (comments in a group, against a logic)
  
What about class based views?
=============================
  
   * Better than function based views because you have inheritance
   
   * django.contrib.admin has good examples of class based views   
 
Reusable frameworks
====================
  
  * an example would be badges
   
  * brabeion
   
  * You can't predict all the ways people want to use your software
  
   * You know the common ways (80/20)
   
   * Provide default behavior and let people swap it out
   
  * django-taggit is his example
   
     * non-integer primary keys
     
     * per-user tags
     
     * official tags
     
     * custom caching managers, or anything else
     
Custom Backends
===============

Many different backend systems

 * django-registration
 * django.core.cache
 * django.contrib.auth
 * django.core.files
 * django.contrib.sessions
 
Libraries approach
==================

 * not everything is business logic
 * Good API design
 * Well defined problem spaces


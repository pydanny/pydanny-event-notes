=======
REST
=======

Gem
===

 * request.raw_post_data

REST has an absence of bureaucracy

Concepts
--------

 * Resources
 * Names (URIs)
 * Representations
 * Connections (links)
 
REST properties
===============

 * Addressable
 
   * Every resource is addressable
   
 * Statelessness

   * Can make requests in any order
   
   * Can make doing transactions a bit challenging (need to treat state as a resource)
   
 * Connectedness
 
 * A uniform resource interface
 
IOW: "Respect the web"
======================

 * RFC 2616

====== ====== ======
HTTP   API    SQL
------ ------ ------
GET    select select
POST   create insert
PUT    update update
DELETE delete delete
====== ====== ======

Adding an API
=============

 * Odds are you already have one! Your website!
 * But cool kids like me (Danny) use JSON
 * use Python 2.6+ version of json over simplejson to get better performance. Same library, just implemented in C.
 * Jacob likes to set mime type during DEBUG to text/javascript to make debugging easier
 
Plain Django
============

 * Jacob likes to construct RESTful resources so he can encapsulate all the RESTy bits in external functions and classes. Keeps his API methods really short.
 
 * In POSTS he remembers to set the right status
 
Piston
======
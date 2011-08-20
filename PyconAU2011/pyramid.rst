=============
Pyramid
=============

by Dylan Jay

Heritage of Pyramid
===================

* Zope => Zope2
* Zope2 => Zope3 begat BlueBreem
* BlueBreem => ZTK
* ZTK => Repoze.BFG (inspired partially by Django)
* Repoze.BFG => Pyramid

* RoR possibly begat:

    * Django
    * Pylons
    * TurboGears

Who uses it?
============

 * Karl Project
 * juice.to
 

Differences between Pyramid and others
======================================

Here we go:

=============== =========== =============
Pyramid         Django      Plone
=============== =========== =============
Not opinionated Opinionated Structured CMS
Very simple     Simple      Complex
No DB           ORM         Custom DB
=============== =========== =============

Sample view
===========

.. sourcecode:: python

    from paste.httpserver import serve
    from pyramid.configuration import Configuration
    from pyramid.response import Response

    def hello_world(context, request):
        return Response('Hello world')

Routes
======

.. sourcecode:: python

    config.add_route('myroute', 'me/{one}')
    config.add_view(hello_world, route_name='myroute')
    
View Callables
==============

.. sourcecode:: python

    class MyView(object):
        """ So much more obvious than Django CBVs!"""
    
        def __init__(self, request):
            # something here I didn't write down
    
        def __call__(self):
            # why doesn't Django do this?
            raise HttpFound('stuff')
            
Renderers
==========

.. sourcecode:: python

    from pyramid.view import view_config

    @view_config(renderer="json")
    def hello_worldrequest):
        return dict(content="hello")

* One of the renderers is a **jinja2** package.

Templates
=========

* Default: Chameleon (latest version ZPT system)
* Can use Jinja2 trivially

Traversal
=========

* I don't really care but the Zope fans seem to love it.
* Works in that you can get things within things
* Some claim you can't do this in Django - but they are wrong. See MPTT.

View Predicates
===============

.. note:: TODO - Look this up later cause I missed it. :P

Security
=========

* Seperation of authentication and authorization.
* You can easily control the security context of a request
* Seems to rely natively on ACL, but you can replace that if you want

.. sourcecode:: python

    # TODO - add example
    config.add_view(myview, name='my-view.html', )
    
See the fun of:

.. sourcecode:: python

    class Blog(object):
        pass
        
    blog = Blog()
    
    blog.__acl__ = [
        (Allow, Everyone, 'view'),
        (Allow, Editors, 'edit'),
        (Allow, Editors, 'delete'),                
    
        ]
        
Scaffolding
============

* Provides a default best practices layout. **Why doesn't Django do this?**
* Very obvious static directory

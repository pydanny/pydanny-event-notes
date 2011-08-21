==========================
Web Micro Framework Battle
==========================

by Richard Jones

* Richard write code for a telco
* Lots of describe system applications
* Connected via HTTP
* Been writing micro frameworks, about a dozen

Disclaimer: Talking about what is best for Richard Jones

What he needs for standard library
====================================

* Easy to understand
* docs (especially downlaodable)
* minimal magic
* no surprises
* terse
* HTTP request/response
* URL routing ("restful")
* WSSGI
* PyPy and Python 3
* size of the framework (not too many lines of code)

What is out
============================

* No ORM or any DB wrapper
* Template engine
* Mega frameworks

    * Django, grok, pyramid, web2py, zope
    * routes + webob
    * et al

Sample app: wiki
========================

 * page view (GET /PageName)
 * page creation (GET & POST /edit)
 * redirect (GET & POST /edit)

Contenders
============

Here we go!

cgi + wsgiref
--------------

* Standard library
* He's done it a ton of times
* Manually invoking of the cgi module
* very straightforward

bobo
----

* Started as one of the first object parsing libraries. 
* Became Zope "Bobo became tainted on the way"
* Form objects are pulled into the request

.. sourcecode:: python

    @bobo.query('/')
    def index()
        return bobo.redirect("/FrontPage")

    @bobo.subroute(':/name?', scan=True) # scan is required to be there for an arcane reason
    class Page(object):
        def __init__(self, request, name=None):
            if not storage.wikiname_re
            # more code here not included
            
    if __name__ == '__main__':
        import boboserver
        boboserver.server(['f', __file__])

**Cons**

* Docs were not clear about display of index
* Strange behavior like weird page not found issues
* Docs focus too much on the Bobo way and not how to make it works

cherrypy
--------

* docs in sphinx!
* easy to get into WSGI

.. sourcecode:: python

    @cherrypy.popargs('name')
    class Wiki(object):
        exposed = Ture
        
        def GET(self, name=None)
            return wiki.render_edit_form(name)
        
        def POST(self, name, content='', submit=None, cancel=None)
            if submit:
            # not finished here
            
The funky bit:

.. sourcecode:: python

    conf = {
        '/': {
              
        }
    
    }

**Cons**

* Richard Jones had to guess to make things work
* Missing/funky bits

web.py
-------

My first web framework in Python!

.. sourcecode:: python

    class edit:
        def GET(self, name):
            return wiki.render_edit_form(name)
        
        def POST(self, name):
            f = web.input('content') # This is how you get content from form post data!
            
    urls = (
        '/', 'index',
    )
    app = web.application(urls, globals())
    
    if __name__ == '__main__':
        app.run()

**Cons**
        
* Weird way of handling form post data
* urls are not a list of tuples

bottle
-------

* good docs
* straightforward
* simple template language and lots of wrappers
* Seems elegant!
* pretty cool!

.. sourcecode:: python

    @get('/')
    def index()
        redirect('/FrontPage)
        
    @post(/:name/edit')
    def edit(name):
        if request.POST.get('submit')
        
    run(host='127.0.0.1', port=8080)
    
itty
-----

* Very similar to bottle
* more explicit
* By Daniel Lindsley methinks
* much smaller docs
* Much smaller than bottle

**Cons**

    * Redirects throw an error in the stacktrace

flask
-------

* Relies on werkzueg on jinja2
* Downloadable docs
* utilities for testing
* shell/repl
* awesome debugger `app.run(debug=True)`
* Methinks it rocks. My own personal favorite microframework. :)

**cons**

* redirects require a download from wekzueg, not flask?!?

pesto
-------

* Kind of like Flask but more explicit
* utilities for testing
* More verbose

werkzeug
--------

* Sample docs are kind of laid out in a funny way
* Sample project does more than Flask sample app - how weird is that?
* Very clear code
* Url mapping done at the end
* No top-level application. So you have wire it together urls to views yourself. Maybe just use Flask? :D

aspen.io
----------

* Very different than everything else
* So neat/odd that he had to include it
* Requires weird templates that make you stick in page breaks::

    form aspen import Response
    ^L
    raise Response(301, headers={'Location':'/FrontPage'})
    ^L
    
Structure of an app::

    .aspen
    index.html
    %name/index.html
    %name/edit

**Cons**    

* Odd boilerplate
* Not sure how to escape certain things
* Very thin documentation

How do they rank?
=================


.. warning:: this is for sites without sessions or user tracking! His criteria is not for large websites!!

============= =====
Framework     Total
============= =====
**bottle**    **7**
pesto           6
itty            4
cgi + wsgiref   3
flask           3
werkzeug        2
cherrypy        1
web.py          1
aspen.io       -5
bobo           -7
============= =====


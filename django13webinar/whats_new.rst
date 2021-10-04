===============
New Features
===============

Templatetags
=============

with
----

New syntax::

    {% with total= objects.count name=request.user.name... %}
    ...
    {% endwith %}

include
--------

New syntax::

    {% include sub/template.html with total= objects.count name=request.user.name... %}
    
Where only specified arguments are included
    
    {% include sub/template.html with total= objects.count only %}    
    
load
-----
    
New syntax::
    
    {% load my_tag from my_tag_lib %}

Also handy bits for future work for making url generation easier::

    {% load url from future %}
    {% url "path.to.view" %}
    
Class Based Generic Views
==========================

http://django.me/generic-views

One of the problems with using class based views is that if you store data in it, then its not thread-safe. Which is why you have to do **MyClass.as_view()** because it makes things thread-safe so always build from something that inherits from the base **View** class.

basic usage in urls.py for direct_to_template::

    TemplateView.as_view(template_name='blah.html')

Detail views::

    class AuthorDetailView(DetailView):
        queryset = Athor.objects.all()

Sample JSON view
-----------------

Here we go::

    from django import http
    from django.utils import simplejson as json
    
    class JSONResponseMixin(object):     

        def render_to_response(self, context):         
            "Returns a JSON response containing 'context' as payload"         
            return self.get_json_response(self.convert_context_to_json(context))
    
        def get_json_response(self, content, **httpresponse_kwargs):         
            "Construct an `HttpResponse` object."         
            return http.HttpResponse(content, content_type='application/json',                                  **httpresponse_kwargs)
            
        def convert_context_to_json(self, context):         
            "Convert the context dictionary into a JSON object"         
            return json.dumps(context)

    class JSONDetailView(JSONResponseMixin, BaseDetailView):     
        pass
    
Should you use CBVs?
--------------------

* With caution
* Use it **ONLY** when you need it.
* **Wait** until some best practices before embracing it wholesale.

Model "on delete" options
=========================

http://django.me/on_delete

The basics::

    author = models.ForeignKey(Person, on_delete=on_delete=models.PROTECT)

On your models if you want to protect the associated model::

    author = models.ForeignKey(Person, on_delete=models.DO_NOTHING)

Only on database fields that are defined to accept null::

    author = models.ForeignKey(Person, on_delete=models.SET_NULL)
    
For setting a new value via a handy sentinel object::

    def get_dummy_person():
    p, created = Person.objects.get_or_create(name='DELETED')
        return p

    author = models.ForeignKey(Person, on_delete=models.SET(get_dummy_person))
    
Testing
========

Resources:

 * http://django.me/testing
 * http://docs.python.org/library/unittest.html

Lots of enhancements to make testing more powerful and more fun. Django 1.3's test framework is built on **Unittest2**.

 * Vastly improved failure messages
 * Easier to skip tests::
 
    class SomeTests(unittest.TestCase)
        @unittest.skip("is always skipped")    
        @unittest.skipIf(*conditional*)
        @unittest.skipUnless(*conditional*)        
        @unittest.skipIfDBFeature(*conditional*)                
        @unittest.skipUnlessDBFeature(*conditional*)                        
        def test_my_stuff(self):
 
 * TestCase.addCleanup
 * assertRaises context manager
 * Class and module-level setup/teardown
 * Backwards compatible
 * assertNumQueries:
 
    * assert number of queries in a views
    * Good for confirming possible performance issues
    * http://django.me/assertNumQueries
    
 * How to make it work::
 
    from django.core import unittest
    class MyTest(unittest.TestCase)
    
RequestFactory
--------------

http://django.me/RequestFactory

So you can test without going through urls or middleware::

    def crazy_test(self):
    
        rf = django.test.client.RequestFactory()
        request = rf.get('/url')
        response = some_view(request)
        self.assertEqual(response.status_code, 200)


Caching backend
================

    * Now supports multiple caches (settings.CACHES)
    * Old syntax works but you'll need to upgrade at some point
    * Features
 
        * Versioning
        * site-wide prefixing
        * transformations
        * pylibmc support - new and faster memcached library
    
Jacob suggests:

 * switch to pylibmc
 * can be tricky to install on some operating systems
 
Static Files
============

 * django.contrib.staticfiles - collects static files from multiple apps into a central location.
 * django.me/static-files

 * **media** Files uploaded by users, probably stored in a FileField or ImageField
 * **static** Static assets that are part of your site - CSS, JavaScript, 
 * **files** Either of the above

In production you have a couple extra steps::

    * Use a dedicated media server (nginx preferred)
    * run `STATIC_ROOT = '/var/www/static'`
    * run `STATIC_URL = 'http://media.example.com/'`
    * run `./manage.py collectstatic`
    
Notes::

    switch existing sites only if you are unhappy
    
Everything else
===============

 * Built in support for Logging (http://django.me/logging)
 * TemplateResponse (http://django.me/TemplateReponse)
 
    * Good for writing decorators that adds in stuff after a view template has been run. 
    * Good for not writing so much page specific middleware
    
 * django.shortcuts.render() (http://django.me/render)
 * Transactions as context managers (kinda neat)
 * "pretty" error emails (???)
 * context-aware simple tags (http://django.me/simple_tag)
 
 
 
================
Django for n00bs
================

by Jen Zajac

* Works for Catalyst
* Uses Sublime 2. So do I!

Introduction
=============

Quotes:

* "*Django is the web framework for perfectionists for deadlines.*"
* "*A framework is something you can hang stuff off of - it is a structure.*"

Frameworks vs CMS's
====================

Frameworks:

* Frameworks take longer to set up
* Frameworks are for specific applications
* Frameworks only do what you plan them to do
* Few wasted features

CMS:

* Take less time to set up
* Broad in design
* Does everything
* Lots of wasted features

.. note:: Did you know that Django was extraced from the Ellington CMS? So the next time someone tells you that Django isn't suited for CMS work, show them https://www.django-cms.org and tell them that http://science.nasa.gov/ is powered by Django (used to be Plone but we rescued it).

Django backstory
====================

* Started in 2003 at LJ World
* Open sourced in 2005
* Hit 1.0 in 2008
* Other frameworks

    * Pyramid (awesome)
    * Zope (over engineered)
    * Bottle (I prefer Flask)
    * TurboGears (IMHO deprecated until it is converted to Pyramid)
    
Pros and cons of Django
=======================

Pros:

* Big community
* Tightly integrated components
* Built-in interface
* Documentation
* Release process
* Authentication & Security

Jen Cons:

* Not playing so well with others

Danny Cons:

* No defined best practices by Django core devs
* Documentation has stagnated in places
* Documentation could use better organization
* Needs to be better at explaining itself as not a framework for programming beginners
* Some WSGI weirdness that is being resolved shortly


Sample model code
=================

.. sourcecode:: python

    from django.db import models
    from django.contrib.auth.models import User
    
    class Movie(models.Model):
        title = models.CharField(max_length=100)
        genre = models.CharField(max_length=100)
        description = models.TextField()
        
    class Attendee(models.Model):
        user = models.ForeignKey(User, related_name="plus") # She used '+' but I'm not sure if this is a good idea. Need to research it!
        
Sample view code
=================

.. sourcecode:: python

    def home(request, template_name="movies/home.html"):
    
        movies = Movie.objects.filter()
        data = {'movies': movies}
        return render_to_response(template_name, data, RequestContext(request)
        
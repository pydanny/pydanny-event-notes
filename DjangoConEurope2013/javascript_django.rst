======================================================
How to combine JavaScript & Django in a smart way
======================================================

by Przemek Lewandowski

    * http://sunscrapers.com
    * Really nice guy, met him earlier this week.

Have you been using JavaScript more and more when building your web applications? Are you implementing REST API frequently? If so, you have probably realised that server-side generated content is no longer enough to provide cutting edge user experience.

I would like to show you how to avoid jQuery callback hell and how to gain more flexibility using MVC on the client side. I will introduce tools for managing modules in JavaScript and will teach you how to become more productive with CoffeeScript. I will share my experience of integrating Django and sophisticated JavaScript stack from two points of view: RESTful API and static files management. Let the trip begin!


Basics
=======

* Django
* Javascript via Coffeescript


Javascript framework considerations
========================================

* Backbone didn't do enough

    * Lack of binding mechanism
    * no reusable views
    * Models are poor

* Backbone & Marionette helped but they were still unhappy
* Angular, very nice
* Ember, very nice

How to use Javascript framework with Coffeescript?
======================================================

* Use requireJS with extra plugins

    * Coffeescript painless integration
    * modular code
    * builder
    * uglifier
    
Tools for building JS apps in Django
=====================================

* django-compressor
* django-pipeline
* django-require

Django & APIs for JS apps
==========================

* django-piston was too long in the tooth
* django-tastypie had an uncomfortable amount of boilerplate
* django-rest-framework was just right.

django-rest-framrwork example:

.. code-block:: python

    # serializer
    class FriendSerializer(serializers.ModelSerializer):
    
        class Meta:
            model = Friend
            fields = ('id', 'name', )

TODO - add examples from our book_

.. _book: https://django.2scoops.org
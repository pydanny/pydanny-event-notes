==================================================
Bleed for Speed: Django for Rapid Prototyping
==================================================

By Rob Spectre

    * http://twilio.com director of evangelism
    * https://twitter.com/@dN0t

Come one, come all to the DjangoCon sideshow to see feats of inhuman speed as we take Django for a spin with rapid prototyping. Tossing security, performance, and maintainability out the tent, Rob Spectre shows a 30 minutes of tips and tricks for building rapid prototypes on Django gained over dozens of hackathons. Find the fastest path from startproject to a publicly accessible endpoint. Discover the reusable apps that cut down your hack's implementation time in half. Marvel at the testing techniques that will minimize demo-killing broken code. Step right up ladies and gents and see the framework forged in the newsroom furnace blast your entirely temporary project across hackathon deadline.

History Lesson
=====================

In the American civil war, there were naval battles. They had boats, and they had the Battle of Mobile Bay. Rear Admiral Bueugard led a fleet in with a simple battle of going between the fort on the left and the mines on the right to bash at the enemy. 

The problem was that during the beginning one of the ships sailed right into the minefield and sunk. The admiral was crazy so would climb to the top of the mast and shout orders to the battle.

In his insanity he commanded the fleet to drive through the mines/torpedoes. And he said, "Damn the torpedoes drive straight ahead". He knew that the mines/torpedoes were old and could be driven through.

**What does this have to do with Django?**

Sometimes when faced with a daunting task, you have to take the bit between your teeth and plow straight ahead.

24 hour prototyping
====================

* Do it outside of hackathons
* Great for tech and concept discovery
* Throw away that code!

Why Django?
================

Rob's claim: Django is the best for rapid prototyping development.

* Django was built explicitly for rapid prototyping development. Out of the newsroom and into production. Today.
* Django is flexible. 
* Django has an incredible community. Have a problem? 

    * Jump on IRC!
    * Read the docs!
    * Stack Overflow!
    * Read `Two Scoops of Django`_!
    
* Bottom line: Gets more stuff done!

How to speed up Django development
==================================

Initial setup
--------------

.. note:: Disclaimer: Rob really promoted our book_. We had no idea before the conference he was going to do this.

* Read `Two Scoops of Django`_ chapter 2 & 3. Much of it is summarized in https://github.com/twoscoops/django-twoscoops-project

    * Suggests add a procfile, which we have as a pull request we may review during the sprints.
    
* You can use Mozilla's Play-Doh as well

Static Files
--------------

* Use the defaults as much as possible
* Nice API
* Bad: Documentation needs revision.
* Brunch (http://brunch.io/) is nice for compiling everything

Deployment
------------

* Heroku is nice, and works in Europe now!
* You can also use AWS: Learn configuration management (chef/puppet/salt stack etc).
* Salt Stack call-out: https://github.com/esacteksab/salt-states 

Packages to use
==================

Build the RESTFUL API
-----------------------

Do it RIGHT away so the front end person can work

* Rob prefers django-tastypie
* These days prefer django-rest-framework now.

Social Auth
-------------

* django-social-auth

    * Gajillions of auth services it supports
    * Takes some work to set up

* django-allauth

    * Fast setup
    * Doesn't have as many auth services it supports
    
* South
* celery

    * Unfair advantage for Python/Django in competitions
    * Setup is a pain
    * **Secret:** You can use the database for hackathons and not worry about setting up a real queue engine
    
Testing
--------

* Why would you test in a short time space?
* **On the contrary:** Why wouldn't you test?
* Knowing your views all return 200 tests means you don't make the same results in writing code or demoing the project

More notes:

* Django tests are fast/easy to write
* AngularJS has a great testing tool. Even if you don't use that many of it's features, check out testacular.

Conclusion
============

When faced with a difficult problem, sometimes its good to plow straight ahead.
    
.. _`Two Scoops of Django`: https://2scoops.org
.. _book: https://2scoops.org    
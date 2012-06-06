========
Keynotes
========

Jacob Kaplan-Moss
=================

.. code-block:: django

    {{ keynote }}

* jacob**@jacobian**.org
* Keynotes are hard.
* Researched to find different types of keynotes

    * Announcements
    
        * Steve Jobs
    * Technical Tour-de-force
    
        * David Beasley style
        
    * State of...
    
        * West Wing style
        * Make it dramatic
        
    * Celebration
    * (Constructive) Criticism
    
        * Cal Henderson's 2008 DjangoCon talk
    
    * Inspiration
    
        * Neil Gaiman
        * Adam Savage
        
Se he's going to do the following talks:
-----------------------------------------

* Technical
* State of...
* Celebration
* Criticism
* Inspirational

Technical Talk
-----------------

.. note:: @jacobian pointed me out and embarrassed me so I didn't finish copying out his sphinx example.

Sphinx is awesome::

    .. code-block:: html+django
        
Useful Sphinx stuff for authentication-protected static files:

    * **static**: http://lukearno.com/projects/static
    * **barrel**: http://lukearno.com/projects/barrel    
    
These sorts of integrated components are an incredible indicator of some of the awesomeness of Python

State of Django Talk
---------------------

* Django is doing very well
* Each release has more and more incredible stuff added.
* "Always feels like we are not moving as fast as we should, but when you look at what's been accomplished it's amazing. Especially since forward compatibility has been pretty well maintained."
* Django 1.5 should give us

    * Python 3 support
    * Composite keys
    
Celebration
-----------

* This year has seen a ridiculous amount of adoption for Django.
* There is no longer an industry where Django does not exist.
* Django is now considered boring compared to things like node.js. Exciting is good when you are trying something new, but "exciting" and "production" should never be combined in the same sentence.

    * See this article http://blog.pinboard.in/2010/01/technical_underpinnings/
    
* Notable tech acquisition for Instagram.

Criticism
----------

* HTML5 issues

    * Bruno's floppyforms handles the form elements for you: see http://django-floppyforms.rtfd.org/
    
* Real-time 

    * State of the art: parallel MVC stacks.
    * Mentioned Meteor framework as state of the art.
    * You are fooling yourself if you don't realize that Meteor style systems are not the future of web development.
    * Are we doomed to callback hell?

.. code-block:: javascript

                    });
                });
            });
        });
    });
        
Can we not do client/server apps purely in Django?
    
.. code-block:: python

    url('people/1/', person_detail)
    
    def person_detail(request, pk):
        ctx['person'] = get_object_or_404(Person, pk=pk)
        return (request, template, ctx)
        
    {{ person.first_name }}

Inspirational Talk
-----------------------

Jacob's uncle, a lawyer asks: "But if you give it away, how will you make money?"

* By giving it away, people have made a ton of money with Django
* Jacob is doing quite well

Summary
----------

* Huge community brought in by our boring, stable system.
* Now we can get really crazy with Django
* Make good art

Karen Tracey - Django and the Community
===================================================

* http://twitter.com/km_tracey
* Been programming since 1987
* Django Core dev for a while.
* Crossword puzzle constructor since 2001
* Cat rescuer since 2009

.. note:: I've been programming since 1980. See http://mytechne.com/user/pydanny/programming-languages/. I win on the age game. So there.

Why?
----

* Django's community is one of it's greatest strengths

Her Django story
------------------

* 2006 she found Django
* Django open-sourced a year earlier
* Django 0.96

Puzzle Database
----------------

* Aid in constructing puzzles, accessible from construction tool
* Amassed over ~5 years
* ~5,000 puzzles, ~100,000 unique entries, ~500,000 clues

Project: Web front-end for database
------------------------------------

* Primary goal: better ability to see data in crossword puzzle tool
* Secondary goal: learn Python

Survey of Python web frameworks in 2006
---------------------------------------

* Pylons
* Turbogears
* Django

Snag: Weird database
----------------------

She wanted to use her old tables instead of Django generated tables. Then she wasn't sure about the code patterns she was exploring.

.. code-block:: python

    class Entry(models.Model):
        entry
        # TODO find the rest of this content
        
She contacted django-users on mailing list and talked to Malcolm and Adrian. Submitted a patch and got it accepted fast.

Sadness
--------

* Probably never happens today that a person contributes so quickly.
* Everything needs tests before submissions are accepted.
* Balance stability with wow-factor

Back to the mailing list post
------------------------------

* She was hesitant to sign her name
* Open source has bad with regard to treatment of women
* Confident of technical ability

    * ... but conscious she didn't know much about web programming
* Would she get more respect if she didn't reveal her gender

Plea: encourage women
-----------------------

* Women actively discouraged from participating in open source communities
* Please don't join in bad behavior
* Speak out against it when you see it

Why did she become so active?
-----------------------------

* Learn more about Django
* Improve communication skills
* Help people
* Puzzles!
* Long range-goal: get a job

What did the Django community gain from Karen's involvement?
------------------------------------------------------------------------

* Lots of triage/bugfixes prior to 1.0
* Some features/bugfixes since 1.0
* Helped many people learn Django

What did she gain out of Django?
------------------------------------

* Become core committer in 2008
* Asked to write a book in 2009 (got published in 2010)
* Got a great job in 2010

Get involved!
--------------

* Community events, big or small
* Mailing lists
* IRC
* Stack overflow
* Ticket triage
* Bug fixes
* Feature development
* Patch review
* Blogs

Jessica McKellar
=================

* http://twitter.com/jessicamckellar
* http://jesstess.com
* Kernal Engineer
* PSF Board Director
* Co-lead of Boston Python

Theme talk
------------------

 * Make me make good choices
 
    * How to make a proper internationalized site
    * Education and best practices by default for novice web developers
    
Accessibility
---------------

* Visual
* Motor
* Auditory
* Cognitive

Visual Accessibility
~~~~~~~~~~~~~~~~~~~~

* 7-10% of Caucasian men haver some form for color blindness
* 2.6% of the global population is visually impaired
* http://www.w3.org/WAI/
* http://www.section508.gov

.. note:: From 2000 to 2010 I was heavily involved in Section 508 implementations for various US government funded projects including http://science.nasa.gov/

Accessibility Guidelines
~~~~~~~~~~~~~~~~~~~~~~~~~

* Alt-text on images
* Accessible intra- and inter-page navigation
* Audio and video accessibilut: captions, transcriptions
* Indicate important info by other things besides just color
* TODO: Finish

See djangoproject.com being fixed! https://github.com/django/django/commit/29a80354ab5e5b85fa37863f70b1cf95646dc699

Django Accessibility
~~~~~~~~~~~~~~~~~~~~

* How can Django help people avoid, detect, and address accessibility issues?
* Set a good example: audit ourselves!

    * Websites
    * Conferences

* Accessibility tutorial?
* Accessibility checklist?
* Warnings on easily correctable issues?

Security
---------

Django handles the following:

* XSS
* CSRF
    
    * But instruction on how to do it with POSTS could be better
    
* SQL Injection

    * Warnings on RAW SQL could be better
    * ORM is EXTREMELY secure
    
* Clickjacking

    * Super easy to enable, but not set by default
    * Documentation on this is kind of buried
    
* Cookies

    * Important things are possibly set the wrong way

django-secure
~~~~~~~~~~~~~~~

* Great little app.
* But if there are that many stupid little things that need to be checked, maybe the defaults should be changed?

How about a security tutorial?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Teach people from the start what they should be doing
* Include a security checklist

Internationalization
---------------------

Done:

* Localization
* Translation
* Timezones
* Django natively supports Unicode data everywhere

django.contrib.auth.models.User
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* First name and last name is very specific to certain Western European nations.
* Work is being done to make the User model properly extendable
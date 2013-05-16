==========================
Growing Open Source Seeds
==========================

By Kenneth Reitz

    * Heroku guy
    * https://twitter.com/kennethreitz
    * https://github.com/kennethreitz
    * Creator of python-requests

This talk will be an in-depth review of the stages that most open source projects go though, and the decisions their maintainers face. Requests will be used as an example — lessons learned and best practices will be covered.

Once upon a time...
======================

The Facebook SDK Python library

    * Facebook rarely updated it
    * Became unworkable
    * People complained, got on Hacker News
    * Disabled comments

Now replaced by http://pythonforfacebook.com

Public Source Projects
=======================

* Company open sources code
* Doesn't maintain it: motivations are unclear
* Really sucks for users of the code

On the other hand.. Gittip!
==============================

* Platform for sustainable development
* Everything is open source, including internal discussions, interviews with media, etc
* Everything is an issue
* Major decisions are voted on github.
* Interviewed with journalists are live-streamed

.. epigraph::

    "I'm not building Gittip, I'm building the community that's building Gittip." -- Chad Whitacre
    
Shared Investments
====================

* Shared ownership, extreme transparency
* New contributors get involved by following a documented process
* Low risk. High bus-factor
* See also: Python, Django, Firefox, jQUery...

HTTP for Humans
=================

python-requests

* One of the most installed PyPI projects
* Key difference between gittip/django and requests: Kenneth makes all the decisions

Dictatorship Projects
=======================

* Totalitarian BDFL owns everything
* Dictator makes all decisions
* Community feedback is encouraged, but users with feedback should have no expectation of change.

Lessons Learned
=================

* Be Cordial be on your way

    * Contributors

        * Keep all interactions with a maintainer as respectful as possible
        * They have likely donated a significant amount of time and energy into their project
    
    * Maintainers
    
        * be immensely thankful to all contributors
        * They are the lifeblood of your project
        * Ignore non-constructive feedback
        * Some people just take things too seriously

Avoiding Burnout
====================

Sustainability
----------------

* One of the biggest challenges for open source
* Everyone has a limited amount of time in the day

Learn to do less
------------------

* When an issue or pull request comes into the repo, two other developers usually triage it.
* This saves an immense amount of time
* I can focus my time on larger issues.
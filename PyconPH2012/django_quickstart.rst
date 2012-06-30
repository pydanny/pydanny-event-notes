==================
Django Quickstart
==================

* By Marconi (@marconimjr)
* on Facebook he is Alexander Peirce
* Wore a github shirt and gave shout out to the pony
* Built off of Audrey's talk. :-)

What is Django?
================

* MTV framework

    * Template = View
    * View = Controller

Demo app
=========

* quickstart.marconijr.com

Set up develop environment
============================

* virtualenv + virtualenvwrapper

.. code-block:: bash

    # .profile on OSX or .bashrc
    export WORKON_HOME=~/Envs
    source /usr/local/bin/virtualenvwrapper/sh

Creating your virtual envuronment
====================================

.. code-block:: bash

    $ mkvirtualenv pyconph
    $ workon pyconph


Installing Django
====================

.. code-block:: bash

    $ pip install Django
    
Create Django project
======================

.. code-block:: bash

    $ django-admin.py startproject quickstart
    $ cd quickstart
    $ python manage.py runserver
    ...
    Development server is running at http://127.0.0.8000
    
Directory structure
====================

.. code-block:: bash

    quickstart
    |-manage.py
    |-quickstart
      |-__init__.py
      |-settings.py
      |-urls.py
      |-wsgi.py


settings.py
=============

.. code-block:: python

    DATABASE = {
        'default': {
            'ENGINE':'django.db.backends.sqlite3',
            'NAME':'dev.db',            
        }
    }

    PROJECT ROOT = os.path.split...


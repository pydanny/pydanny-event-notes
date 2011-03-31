================
Upgrading Django
================

Jacob's process

#. Use virtualenv + pip
#. Upgrade just Django. Don't upgrade other things at the same time.
#. Test and pray you have real unit tests.
#. Upgrade 3rd Party Python Apps
#. Deploy
#. Start adding new features

Upgrade and Test
================

The process::

    pip install -- upgrade Django
    ./manage.py test

This is why having unit tests is a **good** thing. But also click around and test things manually.

Things to watch for
===================


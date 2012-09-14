==========================================
Composability through multiple inheritence
==========================================

Act I: Exposition
====================

* You can use legos to build small things and yet also to build big things.
* Lego block do have the composability feature
* To make components work, you need to have a framework that embodies compositionality.
* UNIX pipes are a good example:

.. code-block: bash

    $ ps aux | grep celery | grep -v grep | ...
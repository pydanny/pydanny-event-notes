==========================================
Python is Only Slow If You Use it Wrong
==========================================

* by Avery Pennarun
* Google employee

    * But this talk has nothing to do with them
    * If you apply to google and say his name he get's money. :)

* Trying to talk about bitter


Stuff he's done
=================

* bup: Python software doing massive things for real problems

    * http://github.com/apenwarr/bup

* sshuttle: VPN software tht handles 802..11 g/n speeds in python

    * http://github.com/apenwarr/sshuttle

Easiest way to do Python wrong
================================

tight inner loops
-------------------

.. sourcecode:: python


    chars = open.file('file').read()
    for char in chars:
        ...
        # slow
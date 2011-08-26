============================================
Giving your website a command line interface
============================================

by Michael Hudson-Doyle

About the presenter
===================

Works for Canonical and Linaro.

Enter Linaro!
--------------

The ARM ecosystem is very fragmented and the kernel has a lot of copy/paste code.

Linaro is a not-for-profit software engineering company investing in core Linux software and tools for ARM SoCs.

see: http://validation.linaro.org/

Why a command-line interface?
==============================

* We want to do things like trigger test runs when a kernal build finished
* This basically means some kind of Remote Procedure Call (RPC)

Need security
------------------

* The boards in our lab are a limited resource
* Some risk of mischief
* Eventually may have test results from unreleased hardware

Protocol Choices
==============================

* They use XML-RPC
* Didn't think about it very hard
* will probably use JSON-RPC

Authentication
==============================

OAUTH
-----

* Hard to implement
* Hard to consume
* Doesn't sign the body of the request in XML-RPC

Used Encryption instead
------------------------------

* Use HTTPS
* Followed RFC 2617 Basic Authentication
* They provide API tokens
* Similar to my Storymarket API work

Live the Server Code
====================

at: https://launchpad.net/linaro-django-xmlrpc

.. sourcecode:: python

    from linaro_django_xmlrpc.models import ExposedAPI
    from linaro_django_xmlrpc.globals import mapper    
    
    class ExampleAPI(ExposedAPI):
    
        def whoami(self):
            return self.user
            
    mapper.register(ExampleApi)
    
Live the Client Code
====================

at: https://launchpad.net/lava-tool

.. sourcecode:: python

    # TODO find a code example
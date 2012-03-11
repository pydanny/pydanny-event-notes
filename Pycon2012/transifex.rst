=============================================
Transifex: Beautiful Python app localization
=============================================

by Dimitris Glezos

Intro
======
 
* Github for translations
* Develop for an international audience

Workflow
=========

* Mark translatable strings
* Release string freeze
* Translator: VCS checkout
* Translate w/special tools
* Get 'em files back

    * SSH, email, tickets

* For every frigging release

Python & Gettext
====================

.. sourcecode:: python

    from gettext import gettext as _
    
    thing = _("I'm going to be translated")
    
.. sourcecode:: jinja

    {% load i18n %}
    
    {% trans "person" %}
    
    {% blocktrans count ppl|length as num %}
    TODO show moar
    
* Generates PO files

How to render PO files
=========================

TODO: show the command-line actions for pure Python and Django
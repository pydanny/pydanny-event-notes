==========================================
Implementing DSLs in Django Apps
==========================================

* by Mattieu Amiguet

Initial Motivation: Searching Contacts
==========================================

.. sourcecode:: python

    class Contact(models.Model):
    
        first_name = models.CharField()
        groups = models.ManyToManyField('Group')
        
* Client wants to customize things themselves
* giving them access to code is dangerous
* Limit their actions

Other reasons
===============

* Quick and easy to implement (if you use the right tools)
* Fun to code!

Not for the end user
=====================

* Only to be used by power users
* Your DSL could be used as a scripting language

How to make a DSL in Python/Django
====================================

* Basics

    * Lexer (vocabulary)
    * Parser (grammar)
    * Some kind of backend

* The lexer and parser part are quite generic

    * use code generator
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
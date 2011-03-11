=========================
Pluggable Django Patterns
=========================

by Corey Oordt

* An app should not be a monolithic pile of code
* A pluggable app is focused

    * It does what it needs to do and nothing more
    * Should have all its dependencies easily described
    * Should be adaptable
    * Should be easily installed

How do you make an app sure is pluggable?
=========================================

* Use small pieces
* types of apps

    * data (manages apps)
    * utility (single functions like pagination)
    * decorator (add functionality to other apps django-mptt, django-taggit)
    

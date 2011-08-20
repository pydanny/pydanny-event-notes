=========
Zookeeper
=========

by Brianna Laugher

**Home grown conference management software**

working example:  http://linux.conf.au

Current System
===============

Not a trivial syste,

* Started in 2007
* Python
* Handles call for papers
* invoicing
* Scheduling
* GPL
* social networks
* special offers
* schedule
* photo competition
* badge printing
* volunteer system
* inventory system

Architecture
============

* Pylons
* SQL Alchemy usually PostGres
* Mako

Roles
=====

* organizer
* core team
* papers chair
* paper reviewer
* funding reviewer
* miniconf organizer
* (user + paid => 'attendee')
* (user + proposal accepted => 'speaker')

Standout feature: Admin reports
===============================

* Amazing report system. **Can't capture them all!**

    * Status of users through the registration process
    * Funding reports
    * Volunteer things
    * A/V release checked report
    * XML metadata for video listings
    * Registrations per state/country
    * tons more
    
Attention needed
=================

* Write tests
* code refactoring
* un-LCA-ficiation (take the Linux conf out of the system,)
* Proposal selection
* scheduling UI
* dashboards
* mail merge
* mobile interfaces
* feedback system

Call to action
===============

* https://github.com/zookeepr/zookeepr
* https://github.com/zookeepr/zookeepr/issues
* irc://irc.freednode/org/#zookeepr
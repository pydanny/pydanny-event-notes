==================
Dynamic Models
==================

by Juergen Schackmann


Django has been built on the assumption to have upfront static data models; i.e. the developer implements them completely before deployment. However, there are numerous real-world uses cases that require to have dynamic models that can be created and amended by users or some kind of user actions. Examples could be: customizable products for a shop, unique content types to represent web site content in a CMS or online surveys that are created on the fly. 

There are various conceptual options to solve this problem. The most prominent ones are: a) Entity Attribute Value Models, b) Pickeld Fields and Pickeld Models, c) Database DDL operations at run-time Most of which have been discussed intensively and the Django community has developed numerous apps. I will compare the various approaches and apps in terms of usability, speed, features, sweet spots and preferred use cases. This will support any future evaluation for a specific project. But it will hopefully also trigger a fruitful community discussion on the importance of this feature for Django in comparison with other applications and frameworks like Zope/Plone, Magento etc.


How to do it
=============

* Entity attribute values

    * Table columns become rows in another table's rows
    * Performance issues

* Serialized Dictionary Django apps

    * Dangerous because of use of Pickle
    * Problematic because of lack of searchability (this is mitigated via tools like PostgreSQL hstore or MongoDB)

* Runtime schema updates

    * Allow updates of the database schema by non-technical user action
    
        * This sounds kind of of risky
        
    * Dynamic models problematic since it can interfere of how the database is designed.
    * Complexity is another issue. How do you keep the database from going nuts from user action?
    * Database integrity is a major issue.
    * Column updates is a really nasty issue. For example, the database has to lock the for minutes or hours.
    
    
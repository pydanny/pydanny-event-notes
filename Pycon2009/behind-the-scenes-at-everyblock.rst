====================================
Behind the scenes at Everyblock.com
====================================

 * Adrian Holovoty
 
Model designs
---------------------

    * Looks straight-forward
    * But can't do models per type
    * So perhaps a bit of abstraction?
        - Entry Attribute Value method?
            * Needs multiple joins
        - Bitmap method uses limited columns
            - varchar01, bool01
            - Needs an in-database schema
            - Sorting can be an issue. Everyblock wrote a custom sort method
    * GeoDjango lets you do geographic queries against your models
    
 * Look up select_template method in Django
 
Data Scraping
------------------

 * Regex for addresses
 * http://code.google.com/p/templatemaker/ (built off C + python)
 * Getting public info can be hard
 
IMPORTANT
-------------

 * June 30th of 2009 Everyblock gets open sourced!
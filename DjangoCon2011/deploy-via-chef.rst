================================================
Real World Deployment using Chef
================================================

by Noah Kantrowitz

 * Ops Code guy
 * Really good at Python!
 * Django hacker
 * Ruby user (tolerates it and not enthusiastic about ti)
 * Developer

Who is here
===========

 * Sys admins
 * Designers
 * Developers
 * Designers
 
How and why
============

 * Infrastructure as good
 * Rebuild a system via a script that includes servers and database
 
    * Configuration management
    * System integration

        * Don't use wikis
        * don't use spreadsheets
        * use code!
        
How does thus work?
-------------------

 * Provision
 
    * Servers
    * Load balancers
    * etcs
 
 * Configure
 
    * Servers
    * Load balancers
    * etcs

About chef
==========

    * Reasonability
    * flexibility
    * libraties and primitives
    
Bits
-----

    * ohai
    * chef-client
    * chef-server
    * knife (command line utility)

..note:: mixed a section here

ecosysye,
----------

    * Apache license 2
    * 400 contrib
    * open source code
    * On github
    
Infrastructure
----------------

    * Recipe
    
        * Have a type
        * have a name
        * have parameters
        * take actions to change state
        * can send notifications to other resources
    
    * Resources
    
        * resources take action through providers
        * What operating system you are on will determine what action is run
        
common resources
----------------

    * `package 'apache2`
    * `template "/etc/apache2/httpd.conf"`
    * `cookbook_file` (Load a recipe that does this sort of thing)
    
Idempotence
-------------

.. note:: what does that word mean anyhow? Ha ha

 * Convergence
 * Gaurd clauses
 
Chef Recipes
--------------

 * Runs just like a script. Doesn;t that make them... scripts?
 * Recipes can include other recipes
 * Extend recipes with Ruby
 

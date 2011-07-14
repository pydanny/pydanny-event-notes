=========================
Django in the real world
=========================

By James Bennett and Jacob Kaplan-Moss

    * What's on the plate
    * testing
    * production environments
    * deployments
    * rest of the web stack
    * monitoring
    * Performance & tuning
 
----

Making your apps reusable for Django
========================================

    * Do one thing and do it well
        - Application == encapsulation
        - Keep a tight focus
            * What does this application do?
            * Should just b one or two sentences
            * Example: Handle storage of users
            * Example: Allow content to be tagged
            * Bad Example: Handle entries in a weblog
        - Even simple Django sites have a dozen installed apps
        - Approach features skeptically
        - What does the application do?
    * Don't be afraid of multiple apps
        - Get rid of the monolithic mindset
            * The application is the whole site
            * Re-use is an afterthoiught
            * Tend to developer apps that are plugins for the master effort
        - Django Mindset
            * Django encourages multiple applications
            * Apps live in the python path so put them anywhere you want
            * Abstraction is provided via Site model
        - Unrelated features should be in their own apps
        - Avoid feature creep
        - Orthogonality
            * Should be able to change one feature without affecting other areas
            * Almost always indicates a the need for a seperate application
        - Reuse
            * There is no such thing as the single case
        - Advantages
            * Don't have to keep rewriting the same bits again and again
            * Can use old work over and over
    * Common Sense
        - Form processing
            * Supply a form
            * But let people specify their own if they want via template parameter in view
            * Redirect after successful submission
            * Supply a default URL
        - URL best practices
            * provide a URLConf in the application
            * Use named URL patterns
            * Use reverse lookup
        - Models (egde cases)
            * whenever possible, avoid hard-coding a model class
            * Use get_model() and take an app labl/model name string instead
            * Don't relty on *objects*; use the default manager
        - Use to love managers
            * Easy to reuse
            * Managers are easy to subclass and customize
            * Managers let you encapsulate patterns of behavior behind a nice API.
        - Advanced techniques
            * Encourage subclassing and use of subclasses
            * Register things like the admin
            * Always consider the API
        - Good API design
            * Pass in a value to change behavior
            * change the value of this setting
        - Bad API design
            * API? What is that?
            * Its open source, just fork it!
    * Build to distribute
        - Project coupling kills re-use
        - Projects should have a settings.py and a URLConf file
        - Make your application package-able even if it's only for your own use
        - Be up front about your dependencies
        - Write for older Python libraries
        - Tell people if you are writing against a stable release of Django or not
    * Be obsessive about documentation
        - It is python: give stuff docstrings
        - Do it lots
        - then do it more
    * Embracing and extending
        - Good applications are extensible without hacking them up
        - Take advantage of everything the language gives you
        - Wrap the code with your own view, this is what decorators are for!
        - Relate other models to it
        - Write subclasses of it
        - You can create proxy subclasses which lets you inherit the code side of things and not the data models.
        - Other tricks:
            * middleware
            * context processrors
        - Be a good citizen
            * If you change someone else's code, be nice about it
            * let the main person know you made the change

----

Testing
===========

At first glance looks like it is about code quality and not deployment. But untested code is broken code. The current standard case is Stupidity driven testing, which is writing tests against the stupidity. So when you find a bug, you write a test to duplicate that bug.

Whatever happens, don't let your test suite break thinking, "I'll go back and fix this later."::

    Unit Testing <---> Functional Testing <---> Browser

You need all the testing tools and methods. You need to test at multiple level.

    * Unit tests
        - whitebox testing
        - verify the small functional units of your app
        - very fine grained
        - familiar to many developers
        - Django.test.TestCase
            * Fixtures
            * Test client
            * Email capture
            * Database management
            * Slower than unittest.TestCase
    * Doctests
        - Easy to read and write
        - produces self-documenting code
        - Great for cases that only use assetEquals
        - Somewhere between unit tests and functional tests
        - Difficult to debug
        - Doesn't always provide useful test failures
    * Functional tests
        - a.k.a Behavior driven development
        - Blackbox or holistic testing
        - Functional testing tools
        - Django.test.Client
            * Close to browser testing
    * Web browser testing
        - The ultimate in functional testing for web applications.
        - Run test in a web browser
        - Can verify JavaScript, AJAX; even design
        - Test your site across supported browsers
        - Browser Testing Tools
            * Selenium
            * Windmill (has built-in Django integration)
    * Exotic testing
        - Static source analysis
        - Smoke testing
        - Monkey testing
        - Load testing
        
----

Deployment
=============

Deployment should...

    * Be automated.
    * Automatically manage dependencies.
    * Be isolated.
    * Be repeatable.
    * Be identicale in staging and production.
    * Work the same for everyone.
    
===================== =========== ==========
Dependency Management Isolation   Automation
===================== =========== ==========
apt/yum               virtualenv  capistrano
easy_install          zc.buildout fabric 
pip                               puppet
zc.buildout
===================== =========== ==========

Look into these tools:

    * virtualenvwrapper (need to modify my .bashrc)
    * pip
    
----

Application Servers
===================
    
    * Apache + mod_python
    * Apache + mod_wsgi
    * Apache/lighttpd + FastCGI
    * SCGI, AJP, nginx/mod_wsgi
    
Unless you have a really good reason, **use mod_wsgi**. Mod_wsgi is much more predictable than mod_python. Web Faction is a good host.

How does scaling work?
-----------------------
 
  * Scaling means that as your load increases, your system speeds up to match.
  
Why separate hardware?

    * Resource contention
    * Separate performance concerns
    * 0 -> 1 is much harder than 1 -> N.

Use connection middleware:

    * Proxy between web and database layers
    * Most implement hot fallover and connection pooling
        * Some provide replication, load balancing, parallel queries, connection limiting, etc
    * Middleware examples:
        * PostgreSQL: pgpool
        * MySQL: MySQL: Proxy
        * Database-agnostic: sqlrelay
        * Oracle: ?
        
Media server traits:

    * Fast
    * Lightweight
    * Optimized for high concurrency
    * Options:
        * Apache?
        * lighttpd
        * nginx
        
Load balancing:

    * Why load balancers?
        - So you can have multiple loads
        - So you can plug-and-play with new/old systems
    * Good traits:
        - Low memory overhead
        - High concurrency
        - Hot fallover
        - Other nifty features...
    * Examples:
        - Apache + mod_proxy (use cautiously)
        - perlbal
        - nginx
        
Monitoring
=============

    * tell me when my site goes down
    * Automatically handle common sources of downtime
    * Ideally handle downtime before it even happens
        - If load gets heavy, kick in new servers
    * Monitor hardware usage to identify hotspots and plan for future growth
    * Aid in postmortem analysis
    * Give pretty graphics
    
----    
    
Availability monitoring principles
----------------------------------------

    * Check services for availability
    * More than just ping yoursite.com
    * Have some understanding of dependencies
    * Notify the right people using the right methods and don't stop until its fixed.
    * Minimize false positives
    
----    
    
Example tools
--------------
    
    - Internal tools
        * Nagios
        * Monit
        * Zenoss
    - External tools
        * Pingdom.com

Usage Monitering
-----------------

    * keep track of resource usage over time
    * Spot and identify trends
    * Aid in capacity planning and management
    * Usage Monitering tools
        - RRDTool
        - Munin
        - Cacti
        - Graphite

Logging and Log Analysis
--------------------------

    * print
    * Python logging module
    * syslogd
    * grep | sort | uniq -c | sort -rn
    * Look into Splunk
    
Performance
=============

*When to care about it*

    * Ignore performance
    * Get the code written
    * Make it work
    * get it on a server
    * then look into it if there is an issue
    
Django slowdowns:
    
    * Look for code using a lot of query
    * Use select_related
    * use caching
    * Look for complex DB queries and look for ways to simplify them
    
The DB is the bottleneck or it will be I/O.

    * Find out what slow means
    * Do testing with tools like wget
    * Sometimes the slowness is actually on front end
    
What to do on the server side:

    * Cache
    * Cache some more
    * Caching turns less hardware into more
    * Caching is a trade-off
        - Do you want to cache everything from everybody?
        - Do you want to only log people logged in?
    * Not all views are the same
        - Clean up your DB queries
        - Use Django's cache middlewhere
    * http://www.revsys.com/writings/postgresql-performance.html
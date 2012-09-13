=====================
Fractal Architectures
=====================

* by Laurens Van Houtven

    * https://twitter.com/lvh
    * Twisted Developer
    * PSF Member
    * Lives in Krakow


Talk Description
=================

Traditional service architecture wisdom generally tells us to build services like this:
    
    * Load balancer in front
    * Web servers, preferably stateless
    * Database (with a caching layer)

That works great for a wide variety of use cases. The point of this talk isn't to deprecate that design, but to discuss a radically different one.

The design I will present in this talk is one consisting of recurring, identical components. It localizes state to individual application servers and persists it to durable stores later. It aims to be easier to scale horizontally: that is, enabling you to increase throughput by simply adding more machines to the homogenous cluster.

I will talk about it's benefits, such as performance and how it fits in well with many cloud providers' services, but also its downsides, such as the inherent complexities of distributed systems. These qualities are analyzed to come to a conclusion about which kinds of project this design is suitable or not suitable for.

In this talk I will discuss both the abstract concepts and the practical implementation that I have built using Twisted and Axiom (a simple object database on top of SQLite 3), which is currently running in production. Although I will touch on the practical implementation, the talk should still be useful for anyone wanting to implement a similar idea using different tools.
    
Standard Architectures
=======================

Check out Twelve Factor App. 

* Level 1: Servers Database Cache
* Level 2: Application Servers
* Level 3: Load Balancing

The problem for you is that scaling all of these levels gets server and code expensive. You have to add in distributed data, messaging queues, and extra servers. Or pay companies like Heroku and dotCloud and Redhat a lot of money.

Consider Instead...
=====================

* Sharding architecture
* Problems:
    
    * Expensive
    * Only for things on a Facebook scale. 
    * Most people don't need this sort of thing.
    * Forces restrictions on code patterns.
    
 * Advantages
 
    * Constraints on code means you have the freedom to do what you want within those constraints.
    * Lower latency
    * Great for when one user is only interacting with data that just affects themselves. For example:

        * Perfect for things like a webmail client. Most of the real behavior of the system is interacting with the client, not doing SMTP.
    
Breaking the rules
==================

.. epigraph::

    Special cases aren't special enough to break the rules.
    However, practicality beats purity
    
    -- Tim Peters, Zen of Python
    
Sometimes it's good to farm things out rather then forcing it into your stack. For example, instead of doing the SMTP yourself, let Rackspace (Mailgun) or Amazon (SMS) do it for you.

The Diablo III example
======================

Auction house could benefit from this architecture.

* Store the data in tiny places per user per general geolocation.
* Would work perfectly using SQLite3 per user if you add in Axiom
* Alternative databases:

    * PostgreSQL
    * Redis
    * MySQL (not recommended)

* Try to use byte-differential storage. Unfortunately, the only professional option for this method is Dropbox. 


Axiom
=======

Links:

* http://divmod.readthedocs.org/en/latest/products/axiom/index.html
* https://launchpad.net/divmod.org
* https://github.com/rcarmo/divmod.org/tree/master/Axiom

Installation caveat: Axiom requires Epsilon in setup.py egg-info, so you need to manually install it first

Info:

 * Runs on top of SQLite3
 * Object database that works with one class per one table.
 * Strongly typed
 * Great for doing queues
 * Does filestore
 * Axiom powerups can have more than just static data, you can add behaviors
 
Manhole
=======

* Twisted project
* TODO: find details as to why he mentioned this

Contention of the Talk
======================

.. epigraph::

    Either make things run faster or make things do less work.

* Query latency between servers (database, caching, http, etc)
* Caching really doesn't work for game servers and processing

**Talk Contention:** If you put it all on a bunch of small servers that can just do their limited collection of tasks, then you get to avoid latency issues between components.

Poking holes in his own design
===============================

* Some of his data doesn't fit into small shards. So things like Encyclopedic data or 'world data' won't work. So where do you put this data?
* Size of data becomes an issue. Small shards hold less data
* Data updates with 10 million user stores means you have to update 10 million datastores

    * You need to keep most of your queries local per shard.
    * This forces tight coupling because a shard needs to really focus on shard data
    
* Querying across stores is hard. :-(

    * Data analytics is harder
    * Big data requires special tools like Hadoop, Apache HBASE, Hive, etc
    
        * Odds are you don't actually need Hadoop. Unless you have terabytes of data you don't need these tools
        
    * Transactions are a challenge. 
    
        * Get the RDBMS to do it
        * You could do it in Python, but that isn't ideal

* No existing tools and frameworks designed explicit for sharding

    * Tools he mentions are general purpose that he uses for this sort of activity
    * Nothing like Django to composite everything together
    * No PaaS (Heroku, dotCloud, OpenShift) to do the system engineering for you

* No load balancing exists that handles this behavior. Which means depending on your setup you're still playing with load balancing.

Testing
===========

How do you do it?

* Careful focus on functional 
* Careful focus on unit tests with mocks
* If you must, use Paxos algorithm to manage the transaction tests
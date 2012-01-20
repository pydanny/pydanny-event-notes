==========================================
Closing session and MongoDB roadmap
==========================================

* by Paul Pederson, Deputy CTO, 10gen
* paul@10gen.com

v2.2 projectedt 2012 Q1
=========================

* Concurrency: yielding and db or collection-level locking
* Improved free list implementation
* New aggregation framework
* TTL collections
* Hash shard key

    * Hashing gives you flat distribution

Concurrency Issues
=========================

* No excessive blocking

    * dropIndex
    * getLastError
    * isMaster
    * etc...
    
* May block for long times

    * foreground index creation
    * reindex
    * compacty (is that a startup name? ha ha ha)
    * repair database
    * creating a very large (many gb) capped collection
    * validate connection
    
Aggregation Framework
========================

* Declarative, no JavaScript reipred
* Pipeline model: $match, $project, $group
* Easy to add new operations
* C++ native (non-JavaScript) implementation

TTL Collections
==================

* Currently: Evict old data to make room for new records by crating a timestamp index, an d create a cron job to delete stale items with update
* Coming: per object or per collection: automates deleting documents older than some limit.

Harsh Shard Key
====================

* **If** you are not expecting range queries on the shard key
* **Then** it makes sense to shard by hask key, you naturally get a flat distribution
* In a sense this is the easiest possible case
* Mongodb started by solving the hard case.

Short List (not in 2.2 but coming up)
======================================

* Full text Search (so you don't need SOLR)

    * The absolute number one requested feature
    * Done but needs to be vetted and tested better
    * Text searches can generate bajillions of extra records and other issues
    * Sounds like they are trying to do it right.

* More concurrency
* Online compaction

    * Make the system smaller on the fly
    * This way you don't have to play replica set games to clean things up

* Internal compression
* Read tagging

10gen Hiring
=============

* NYC/Silicon Valley - may see us
* EU

    * London
    * Dublin

* Anywhere - Language Evangelist
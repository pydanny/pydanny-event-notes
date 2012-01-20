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

Reasons
=======
 * http://blog.codejams.net/pycon/
 * Performance boost over Sqlite + SQLAlchemy

Example: Invoice
================
 * Invoices have lineitems
 * lineitems may be split into accounting codes
 * invoice has payments
 * Must record amount paid on each accounting code for AR
 * Invoice/lineitem
 * simple JSON creation

Implementation
==============
 * Choose a way to persist string keys and string values
 * Choose a serialization format
 * Add features as 'middleware'
 * add querying by wrapping our db in a MapReduce implementation
 * Serve our database over HTTP using WSGI
 
Storage: Roll your own
======================
class DictMixin(object):
    def keys(self): pass
    def __getitem__(self,key): pass
    def __setitem__(self,key,value): pass
    def __delitem__(self,key)__: pass

Other ideas::
    * Use gdata, amazon, or other on-line db

Ways
====

dumbdb::
 * written in Python, a flat file
 * fallback option

dbm::
 * Unix only
 
gbdm::
 * Non-standard format
 
dbhash::
 * BSD DB library
 
Shove::
 * Recommends shove which lets you use various Amazon, gdata and other handy ways. 
 * Found on cheese shop
 
Tradeoffs
==========
 * Scaling
 * Editing of data
 
Serialization
=============
 * cPickle
 * marshal and repr/eval is not safe
 * JSON - yay!
 * YAML
 * XML
 
Serialization tradeoffs
========================
 * interoptability
 * speed (cPickle, JSON are fast)
 * security
 
Adding features
===============
class UserDict(object): pass
class JSONSerializer(UserDict)
Use formEncode to validate a document has the correct schema

Data replication & versioning
==============================
class VersionDict(UserDict):
    def __getitem__(self,key): do magic code
    def __setitem__(self,key): do magic code

Map-Reduce Querying
===================
 * use Google's tool to handle storage and data optimization
 
The server
==========
 * class HTTPDict(UserDict): lots to do (disk space, memory usage, parallelizing, concurrency, locking, transactions, many others)
 
Summary
=======
 * Worse is faster and in some ways better
 * UserDict amd DictMixin are fascinating
 * Document oriented databases are fascinating

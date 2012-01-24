==========================================
Running MongoDB in the Cloud
==========================================

* by Dan Crosta, Software Engineer, 10gen
* I know speaker from twitter and him answering questions about MongoDB to help me with http://consumernotebook.com

.. note:: Late cause we were intercepted by Redhat/OpenShift marketing who wanted our advice on logos.

MongoDB components
===================

* Config Servers send config data to shards
* Shards can run with the config server down, but it is not fun.

Replica Sets
=============

Different methods of setup:

#. The most popular

    * Primary
    * Secondary
    * Secondary

#. Another way

    * Primary
    * Secondary
    * Arbiter

#. The big option

    * Primary
    * Secondary
    * Secondary    
    * Secondary
    * Secondary    
    
Amazon EC2 Instance Types
============================

.. warning:: Never deploy with 32-bit. Don't do it!!!

* Go for a Large or Extra-Large on-demand instance. More expensive but worth it.
* ConfigD / Arbiter can be done via micro on demand instances

Operating System
==================

* Use ext4, xfs
* Use RAID:
    
    * Raid 10 on MongoD
    * Raid1 on ConfigbDB
    
* Turn off atime

    * File descriptor limits::
      
      cat >> /etc/security/limits.conf << EOF
      * hard nofile 65536
      * soft nofile 65536
      EOF
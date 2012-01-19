==========================================
Running MongoDB in the Cloud
==========================================

* by Dan Crosta, Software Engineer, 10gen
* I know Dan Crosta from twitter and him answering questions about MongoDB to help me with http://eandatabase.org

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

# Another way

    * Primary
    * Secondary
    * Arbiter

#. The big option

    * Primary
    * Secondary
    * Secondary    
    * Secondary
    * Secondary    
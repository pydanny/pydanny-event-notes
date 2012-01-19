=======================================
Diagnostics & Performance Computing
=======================================

by Dan Crosta, Software Engineer, 10gen

Speed
=====

* MongoDB is a high performance database
* But how do you know you are getting the best performance

Tools
=========

#. mongostat

    * tons of useful columns 
    * mapped
    * vsize
    * res
    * faults - how many disk faults
    * locked %
    
        * In a given window of time, measures two things (TODO find out)
        * Rough percentage measure - not perfectly accurate
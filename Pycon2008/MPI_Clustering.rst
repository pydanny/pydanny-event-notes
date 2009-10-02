Netflix Prive
=============

 * Use Pyflix library to squeeze dataset into 600MB
 * http://pyflix.python-hosting.com
 
More CPUs
=========
 * Some algorthms take weeks
 * Need runs over many sets of data
 * Problem if your resources are limited
 
Beowulf Clustering
==================
 * Expensive
 
Amazon EC2
==========
 * __init__(Amazon Machine Images)
 * Pay for what you use
 * About $0.10 per hour per small box, 0.80 for that

Parallel programming in Python
==============================
 * basic prototyping done in Numpy
 * Find clustering stuff to extend it
 
ElasticWulf
===========
 * Cheap
 * copies Beowulf but uses Amazon EC2 to handle stuff

What is MPI?
============
 * Use Ipython1
 * High performance message passing interface (MPI)
 * Implemented in multiple languages
 * Point to point collective operations
 * Very flexible and complex
 
Basics of MPI
=============
 * Each process has a size attribute: num of operations
 * Each process has an id attribute
 * import mpi
 * local_array = mpi.scatter(my_list) # runs a list of functions across multople systems
 * root_date = mpi.gather(local_array) # grabs the data from the processes
 
Getting started
===============
 * Sign up for Amazone Web Services
 * Get your keys/certs
 * Download Elastiwulf python stuff
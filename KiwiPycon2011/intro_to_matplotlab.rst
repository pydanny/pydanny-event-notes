============================================================
Introduction to Matplotlib for Data Analysis
============================================================

by Catherine Thwaites

Why Matplotlib?
================

* Great way to visualize complex data
* Free
* Fast
* Works on any OS

Dependencies
=============

 * Python 2.5., 2.6, 2.6
 * Numpy 1.3+
 * Matplotlib 1.0.1
 
Install
========

Linux: http://matplotlib.sourceforge.net/users/installing.html

Windows: Download and install

On-line Examples
==================

Huge gallery of examples!

* http://matplotlib.sourceforge.net

Ways to run matplotlib
=======================

* Interactively with pylab and python
* Interactively with the shell
* Normal Python modules
* Some other way?

Simple bargraph using bar
=========================

.. sourcecode:: python

    import numpy as np
    import matpltlib.pyplot as plt
    data1 = [12,23,38,42,41]
    figure = plt.figure(1, (6,6))
    figure.clf()
    ax = fig.add_subplot(111)

    ind = np.arange(len(data1))
    rects = ax.bar(ind+0.125, data1, width=0.75, color='thistle')
    plt.show()
    
Clarified versionL
    
.. sourcecode:: python

    import numpy
    import matpltlib.pyplot as plot
    data1 = [12,23,38,42,41]
    figure = plot.figure(1, (6,6))
    figure.clf()
    axis = fig.add_subplot(111)

    ind = numpy.arange(len(data1)) # what is ind representing? An index?
    rects = axis.bar(ind+0.125, data1, width=0.75, color='thistle')
    plot.show()    
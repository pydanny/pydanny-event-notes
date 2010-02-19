Torguga
=======

University of Maryland

Details
---------

 * Python
 
   * 15,000 SLOC
   * AI, GUI
   
 * C++
 
   * 50,000 SLOC
   
30 member team

What does Tortuga do?

 * Competes in competitions
 * Does not leak
 * Drives under water
 * see and move around obstacles
 * home on sounds
 
Construction

 * 6 thrusters
 * Pressure vessel with a Mac Mini, batteries, custom electronics
 * Runs Gentoo Linux
 * 4 hydrophones
 * Grabber used as a claw

Python
--------------

 * Great flexibility and unit testing support
 
 * compact code
 
 * easy to learn - easy to get new members up to speed
 
 * stdlib and 3rd party support helped a lot
 
Unit Testing
-------------

 * No 3rd party library to install and manage
 
Woes
------

 * C++ integration
 * Boost.Python and Py++ are powerful, but complex
 * Overheard for wrappers is large in terms of dependencies, disk space, and compile time
 * Small bugs and compiler incompatibilities lead to fragile bindings
 
The GIL
-----------

 * Inflexible nature gratly constrains concurrent system design
 * Forced the core of our software into C++
 * C++ calling back into python is especially likely to run afound of the GIL
 
GUI & Simulator
------------------

 * Done in wxPython & Python-Ogre
 
Dependency Management
---------------------

 * Build things with a custom script


Conclusion 
----------
 * Dynamic languages are great fit for dynamics problems

 * Python is great for robots because of their dynamic nature

 * State.py is their AI library
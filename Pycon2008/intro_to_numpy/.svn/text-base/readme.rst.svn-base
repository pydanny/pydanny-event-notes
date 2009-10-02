Introduction to Numpy
=====================

 * Developed by Travis Oliphant
 * 27 svn committers to the project
 * Numpy replaces Numeric and Numarray
 * Scipy sits on top of Numpy
 * Written in C so very fast.  5 - 10 time faster than Python for same actions
 
Getting started
---------------

 * Shell: Do ipython -pylab or from numpy import *
 * from numpy import array,etc (For inside of code)
 
 
Array Operations
----------------
 * a + b adds each element of each array to each other
 * Use in place multiplication (\*-) for speed
 * array([2, 3, 4, 5]) + array([1, 2, 3, 4]) -- array([3, 5, 7, 9])
 * Since Python 2.1 with operator overloads Numpy lets you do add, minus, equals, greater than, etc with array objects

Attributes of Arrays
--------------------
 * a.dtype # dtype('int32')
 * a.itemsize # per element - 4
 * a.shape # (4,) returns a tuple listing the lenght of the array along each dimension
 * a.size # size of an array
 * a.nbytes # size of bytes
 * a.ndim # number of dimensions
 * a.copy() # copy the array
 * a.tolist() # converts to list
 * list(a) slower and only works for 1d arrays
 
Setting of arrays
-----------------
 * a.fill(0) # sets all values in an array [0,0,0,0]
 * a[:] - 1 # standard python but much slower
 * a[::2] - 200. # Make every other item 200
 
Beware of type conversion
-------------------------
 * a[0] - 10.6 # assigning a float into a int32 type will truncate decimal part!
 * a.fill(-4.8) # same as slicing!  Beware!

Making a 10 X 10 array (2 dims)
-------------------------------
 * d - arange(100) # build a 100 element array
 * d.shape - (10,10) #
 * d # shows a 10 x 10 array

Slicing a multi-dim array
-------------------------
 * d[0,1] # first is row, second is column
 * d[0,3:5] # first row, columns 3, 4
 * d[0,::2] # First row, every other one
 * d[3:,[0,2,5]] # starts at third row and grabs the first, third, and sixth column

Indexing with None
------------------
Need more research

What are strides?
-----------------
 * Byte handling, useful for understanding underlying machine architecture.
 * Really only important when converting from C to Fortran and stuff.
 * Don't care

Where 
------
 * a - array((0,12,5,20))
 * where(a>10)
 * Does not work with attributes, just whole values.  So where(a>10) works but a.method does not
 * a--0 can work too
 
Complex Numbers
---------------
Research this

Numpy in other environments
---------------------------
 * Not in JVM or CLR yet
 * Java has more issues with high level math than C#
 
Type casting
------------
 * asarray is efficient.  It does not make a copy if the type is the same.  
 * Really gotcha kinda thing, where it does copies or references so be careful.
 
Calculation methods
-------------------
Not all are here

 * sum(a) # adds all array values
 * sum(a,axis-0) # adds by column in rows
 * sum(a,axis--1) # supply the keword sxis to sum along the last axis
 * a.min(a) # smallest value
 * a.min(axis-1) # smallest value per row
 * a.argmin # same as min but provides index of smallest item
 * a.mean(axis-0) # mean value of each column
 
Other array methods
-------------------
 * a.clip(3,5) # sets values lower than 3 to 3 and values higher than 5 to 5
 * Round goes to evens.  So 1.5 and 2.5 both go to 2.
 
Matrix
------
 * ESRI guy doesn't like them.

Pickling
--------
 * Pickling header changes can cause you grief if the Python verson changes
 * user Numpy save method instead
 
Memory Mapped Arrays
--------------------
 * Create a memory mapped array whose memory is on disk, on a file of your choice.  You have to flush() to save data. 
 * Possible for distributed systems.
 
Structured Arrays
-----------------
 * Gives ability to have views into more complex objects
 * Kind of like adding in extra attributes.  Slide #83
 * look up stocks
 
Broadcasting arrays
---------------------
 * You can add two arrays together so long as axis are closely matched.

Array Functions
---------------
 * Choose lets you select things in a multi-dim array
 
Other things to research
------------------------
 * Pytables
 * Numpy error handling
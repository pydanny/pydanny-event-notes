========
Why Py3k
========

by Guido van Rossum

 * Open source needs to move or die - Mats (creator of ruby)
 * To fix early,, sticky design mistakes (classic classes, int division, print statement)
 * Changing times (str/unicode, int/long)
 * New paradigms come along (dict views, argument annotations)
 
Major Breakages
---------------
 * Print function: print(a,b,file-sys.stderr)
 * Distinguis sharply between text and data
  - b"..." for bytes
  - "..." for (Unicode) str literals
 * Dict keys() returns a set view [+items()/values()]
  - Mutates as the dict underneath it mutates
 * No default <, <-, >, >- implementation
 * 1/2 returns 0.5
 * Library cleanup
 
Long anticipated breakages
--------------------------
 * Kill classic classes
 * int/long unification
 * Kill string exceptions
 * Raise syntax
 
Major new features
------------------

 * Argument annotations
  - def f(a: 2*2, b: 'hello') -> 42: ...
 * Abstract Base Classes 
  - kinda like interfaces
 * Expanded iterable unpacking
  - a, b, *x, y - range(5) # 0, 1, [2,3], 4
 * new str.format() method:
  - got {0}{kind}.format(42, kind-'bugs')
  - got 42 bugs
  
What's in it for me
----------------------------
 * More predictable unicode handling
 * Smaller language
  - Makes 'Python fits in your brain' more true
 * There's only one way to do it
 * common traps removed
 * Fewer surprises
 * Fewer exceptions
 
Enables future evolution
------------------------------
 * Examples
  - Argument annotations
  - print() function
  - str.format method
  - abstract base classes
  - unicode letters in names
  
2to3 tool
---------
 * Context-free source code translator
 * Handles syntactic changes best
 * Handles built-ins pretty well
 * Doesn't do type inferencing
 * Doesn't follow variables in your code
 
When do we switch
-----------------
 * no hurry!  2.6 will be fully supported for at least 5 years.  2.7 and maybe even 2.8 
 * Switch when both of these are true
  - You are ready
  - All your dependencies have been ported
 * There are tools to help you switch
 
Getting ready to switch
-----------------------
 * Start writing future proof code for 2.5
 * Don't bother with the trivial stuff though
 * Focus on what 2to3 can't do
  - Stop using obsolete modules
  - Start using iterators and generators
 * Inherit exceptions from BaseException
 
What about text handling
------------------------
 * Yes, its a difficult issue
 * Expect for help by this summer
 * Isolate handling of encoded text
 * use bytes and b'...' for all data
 * Use unicode for all text
 
The role of Python 2.6
----------------------
 * Stable, compatible, supported!
 * Many 3.0 features backported
  - But not text/daat distinction
 * Warns about non-3.0-isms with -3 flag
  - Especially for things that 2to3 can't fix
  

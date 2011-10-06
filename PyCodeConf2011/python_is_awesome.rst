====================
Future is Bright
====================

.. note:: Watched this at PyCon AU. Copied over my notes from there so I can fill in the holes here.

* By LA Python's own Raymond Hettinger

Context for Success
---------------------

 * License
 * Commercial Distributions
 * Zen
 * Community
 * Repository of Modules (PyPI)
 * Killer Apps and Success Stories
 * Win32
 * Books
 
License
--------

 * Most Python releases are GPL-compatible. This makes it free.
 * Going to a closed source language means you are trapped. 
     
Community
---------
    
    * Mailing lists
    * Newsgroups? HA HA HA
    * Python User Groups
    
PyPI
----

    * Repo for Python programming language
    * Over 16,000 packages
    * `pip install ordereddict` works for Python 2.5!
        
Killer apps
------------
    
    * Zope, Django, Pyramid
    * Numpy and Scipy
    * Bittorrent and Twisted
    * YouTube
    * Blender and Maya
    * Win32 - Factoid: Me, @pydanny, has done all his windows programming using cpython and Win32!
        
Easy to learn!
---------------------
    
    * Good teachers.
    * Think how fast you got the types and control structures in Python. General 3 hours
    * In a day you can learn special methods and stdlib
    * Critical because if you need good Python developers it doesn't take long to get up to speed. Converting developers takes:
    
        * C takes 2 years to get competent
        * Java takes 6 months to get competent
        * Python takes a week to get competent
        
    * Rapid development cycle
    
        * Scripting languages are unbeatable for development speed
        * Programs are grown organically
        * Interactive testing lets people work with their code results immediately.
        * Bang out real code fast
            
Economy of expression
---------------------

 * Not many words or characters to get things done.
 * clear English means non-coders can understand your work
 * **Pydanny factoid**: One of the first times I wrote Python on a whiteboard for a boss at NASA/SAIC they thought it was very legible pseudo code representing a complex process.
    
.. sourcecode:: python

    hashmap = {}
    for path, dirs, files in os.walk('.'):
        for filename in files:
            fullname = os.path.join(path, filename)
            with open(fullname) as f:
                d = f.read()
            h = hashlib.md5(d).hexdigest()
            filelist = hashmap.setdefault(h, [])
            filelist.append(fullname)
    pprint.print(hasmap)
            
Beauty Counts
-------------

 * Readability is the #1 mentioned characteristics of why organizations choose Python
 * The beautiful appearance on the page directly affects a programmer's sense of joy
 * Makes us go home and write code
 * If you can read other people's code that makes it easier to maintain
 * Because we all `mostly` share the same idiom it means we can read each other's code. That doesn't stifle creativity - it just means we can get along.
 
    * As a parent I can say I would have *loved* having a formal uniform at school. As a geek in school I would have loved that too. :P

Interactive Prompt (REPL)
----------------------------------------

    * Python experts don't memorize Python
    * They use the interactive prompt often (I try to write tests...)
    * This is a killer features that runs circles around compiled languages
    
        * Python shell
        * IPython 
        * BPython (My favorite)

Behind the Scenes
------------------

Philosophy of core dev

 * Conservative growth
 * `We read Knuth so you don't have to`
 * Aim for simple implementation
 
Protocols
----------

To interact with these we have defined protocols

 * DBAPI
 * Hashlib
 * Compression
 * WSGI for the web
 * Conversion protocols

Specifics of Python: The Foundation
------------------------------------

 * Dictionaries and Lists
 * Automatic memory management
 * Overridable syntax
 * Exceptions
 * **You can reprogram the brackets?**
 * **And we can reprogram the dot?!?**
 
Winner Language Feature: Iterator Protocol
------------------------------------------------

 * High level glue that holds the language together
 * Iterables: strings, lsits, sets, dicts, collections, files, open urls, csv readers, itertools
 * Um... I know this. I've had to construct these on my own in other languages. But not Python... Wow - I just realized this just now.
 
.. sourcecode:: python

    # When Raymond wrote **sorted** he wasn't thinking about sets
    # But they still just works
    sorted(set('abracadabra'))
    sorted(set(open(filename))
    sorted(set(open(filename))
    
.. warning:: If you say "Python has iterators, you have to explain how it is globally implemented. Other languages have iterators, but they have to be implemented and extended and stuff"

Winner Language Feature: Generators
--------------------------------------------

* List comprehensions give us joy
* Logical extension to list comprehensions and generators to unify the language
* List generators are amazing. No one else has them
* Serious magic
* A million rows in a generators is nothing
* Simple syntax to do them. You only need the YIELD keyword.

.. sourcecode:: python

    # Sample generator code
    def pager(lines, page_len=60):
    
        for lineno, line in enumerate(lines):
            yield line
            if lineno % pagelen == 0:
                yield FORMFEED

    # genexps setcomps and dictcomps
    sum(x**3 for x in xrange(10000))
    
.. note:: I've used list generations to super-optimize slow code

Proposal: Generators that accept inputs
----------------------------------------

* Generators support **send(), throw(), close()**
* Unique to Python
* Makes it possible to implement **Twisted**'s *inline deferreds*
* Add one line of **Twisted** to your code and it infects your whole app

    * Twisted forces you to write in callbacks
    * Callback coding is hard to follow and debug
    * Wouldn't it be great if we could have the benefits of Twisted in procedural code?

.. sourcecode:: python

    # two way generator example
    @inlined_defereed
    def session(request, cleared=False):
        while not cleared:
            cleared = yield authenticate(request.user)
        db_result = yield database_query(request.query)
        html - yield format_data(db_result)
        # TODO finish getting this down
        
Winning language Decorators
------------------------------

 * Expressive
 * Easy on the eyes
 * Works for functions, methods, and classes
 * Adds powerful layer of composable tools
 * **Factoid**: I have problem writing them. Serious problems. :'(
 * Raymond shows sample code from Daniel Lindsley's Itty!
 
    * https://github.com/toastdriven/itty

Winning Language Features: exec, eval, type
--------------------------------------------

 * Not a fan of `exec` and `eval` because when used in my experience they are done badly
 * But `type` is awesome
 
Winning Language Feature: With Statement
------------------------------------------

    * Clean, elegant resource management: threads, locks. etc
    * Important tool for factoring code
    * Contains the setUp and tearDown code.
    * The reverse of functions

Winning Language Feature: Abstract Base Classes
--------------------------------------------------

 * TODO - go over this one
 
Winning Language Feature: Indentation 
--------------------------------------------------

 * Makes the code really clear
 * We write our pseudo code this way
 * Less errors!
 * Less ambiguity!
 
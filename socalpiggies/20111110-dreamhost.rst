===============================================
June 6, 2011 - Socal Python meetup at Dreamhost
===============================================

.. note:: Arrived 30 minutes late so my notes are woefully incomplete

Asynchronous programming techniques in Python
===============================================

.. note:: My normal answer is to use Celery + Redis/RabbitMQ to handle this stuff. Is that cheating? ;)

by TODO: ask the name of speaker

* *Walked in the on the part about Twisted...*
* Threads vs processes are a debatable issue.
* Cost of using Python to create new processes is considered slow
* Blocking and memory access issues
* Async is a problem in Python because not all libraries support it
* Someone mentioned a library called *pystates*
* GIL

    * Multiple threads in Python are OS processes and you can get blocking on memory objects
    * On large processes on things like `dict` hash-tables you can get blocks/locks on the wrong thing
    
Multiprocessing
----------------

* Called 'giant hack'
* Looks likes the threads API
* Uses a messages system to use OS processes to share data between processes/threads
* Uses pickles to share data via messages, which means anything that is deserialized executes the code

    * Which means you should watch out for code injection!

Communicating Sequential Processes
------------------------------------

* Title of an academic paper
* A system of sharing tasks and data

Gevent
------

* Wonderful monkey patch that does the bulk of the work needed for multi-tasking.
* Does not use threads, replaces certain libraries on the fly.
* Uses co-routines, built on lib-eb
* I've played with it, and it is fun.
* See:

.. sourcecode:: python

    monkey.patch_all()
    
.. note:: See my notes on Gevent at http://pydanny-event-notes.readthedocs.org/en/latest/KiwiPycon2011/python_dist_gevent_redis.html

Metaclasses: Look behind the curtain
============================================

by Dreamhoster John LaCourt

.. note:: Presenter is saying it's not magic, I agree. However, IMO, 95% people use Metaclasses, they have no reason to do so. So I listen to this talk with concern because debugging bad Metaclass code is a pain.

What does a class do?
-----------------------

* Class constructs are called instances
* What does it really mean to construct an instance?

    * A class provides an instance with it's namespace
    * Attributes of a class define the namespace of the instance
    * Example of a class:
    
.. sourcecode:: python

    class Person(object):
        greeting = 'hello'
        
        def greet(self, who):
            print self.greeting, who
            
    j = Person
    print j.greet('SoCal')
    'hello SoCal'
    
Example libraries
-------------------

* SQLAlchemy
* FormEncode
* Django ORM    
    
What is a metaclass?
----------------------

    * A metaclass is a class of a class
    * A metaclass is a class whose instances are classes
    * This is called metaprogramming
    
The `type` metaclass
----------------------

* If the instance of a metaclass is a class, can we insubstantiate the class just using `type`

.. sourcecode:: python

    def greet(self, who):
        print self.greeting, who
        
    Person = type(
        'Person',
        (object,),
        {'greet': greet, 'greeting': 'Hello'}
    
    )
    
    j = Person
    print j.greet('SoCal')
    'hello SoCal'    
    
First metaclass:

.. sourcecode:: python
    
    class MyFirstMeta(type):
        def __init__(cls, name, bases, ns):
            cls.uses_my_metaclass = True
            
        def mystery_method(cls):
            # All methods in metaclasses are metaclasses, which is why 
            #       the variable is 'cls' and not 'self'
            return 'I am a myster method'
        
    # the grungy way of building that class    
    MyClass = MyFirstMeta(
        'MyFirstMeta',
        (object,),
        {'greet': greet, 'greeting': 'Hello'}
    )
    
    # the easier way of building that class
    class MyClass(object):
    
        __metaclass__ = MyFirstMeta
        
Practical example
--------------------

* Enforce all the things, like in Java

.. sourcecode:: python

    class Field(object):
    
        def __init__(self, ftype):
            self.ftype = ftype
            
        def TODO: #get this method
            pass
    

    class EnforcerMeta(type):
        def __init__(cls, name, bases, ns):    
    
            cls._fields = {}
        
            for key, value in ns, items
                if isnstance(value, Field):
                    cls._fields[key] = value
        
    class Enforcer(EnforcerMeta):
        __metaclass__ = EnforcerMeta
        
        def __setattr__(self, key, value):
            if key in self._fields:
                if not self._fields[key].is_valid(value):
                    raise TypeError('{0} is not valid'.format(key))
            super(Enforcer, self).__setattr__(key, value)
            
    class Person(Enforcer):
        name = Field(str)
        age = Field(int)        

Great! Now be @#$%ing careful!!!!
------------------------------------

* Because they are constructing classes on the fly, bugs in your metaclasses will often happen during import statements
* Please, please use them judiciously
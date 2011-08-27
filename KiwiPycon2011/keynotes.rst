========
Keynotes
========

Python in the Web: Can we keep up?
==================================

By Audrey Roy

*I'm partial but I think she did a great job of pointing out where Python might/should go.*


Metaprogramming
===============

By Jeff Rush

"*Metaprogramming is the programming of programming*"

.. note:: Apologies, but I couldn't keep up with the firehouse of knowledge. This is woefully incomplete.

.. warning:: This is from me: Metaprogramming should be done carefully. Only use it when you have no other options!

This talk makes use of
----------------------

    * metaclasses
    * decorators
    * attributes
    * more
  
What is metaprogramming orientation
-----------------------------------

  
 * Code **Manipulates** Data
 * Data **Feeds into** Code
 * Metaprogramming sits about the Code/Data
    
        * Add/adjust elements
        * register elements
        * tag elements
        * event management
        
            * Pre/post initialization
            * read/write
            * call-and-return
            
Addressing a problem
--------------------

.. sourcecode:: python

    class Request(object):
        
    class HTTPServer(object):
        def handle_request(self, ...):
            req = Request(...)
            
* objective

    * subclass a class deep inside a module
    * Requires rearrangement content of the module

.. sourcecode:: python

    old_import = sys.modules['__builtin__']
    sys.models['__builtin__'].__import__ = self.__import__
    
Sample code
-----------

.. sourcecode:: python

    class Member(object):
        __metaclass__ = DatabaseTable
        
        dbtable = "Members"
        
    class DatabaseTable(type):
    
        def __init__(cls, name, bases, class_dict):
            col_defs = db.query_cols()
            for col_def in col_defs:
                db_column = wrap_col_rdwr(col_def) 
                setattr(cls, col_def.name, db_column)
    
    def wrap_col_rdwr(col_def):
        def get_dbcol_value(self):
            return self.__dict__.get(col_def.name, None)
            
        def set_dbcol_value(self, value):
            value = col_def.validate(value)
            self._-dict__[col_def.name] = value
            
        return property(get_dbcol_value, set_dbcol_name)
                

Meta classes? class decorators
--------------------------------

* The latter are much simpler
* The latter can do almost everything the former can

    * only a metaclass can add methods to the class itself
    
* class-level services (methods)

    * @classmethods provide them to instance
    * metaclass methods provide them to the class itself
    
* only a metaclass can add to class attrs not visible to self

    * meta-methods
    * meta-properties
    
* Class decorated can be (more easily stacked)
* MISSED BULLET

Example using class decorator
-----------------------------------

.. sourcecode:: python

    def CallTracer(attr):
        """ Do custom logic stuff here """
        return attr

    def tracecalls(cls):
    
        def my__getattribute(self, name):
        
            attr - super(cls, self).__getattribute__(name)
            return attr if not callable(attr) else CallTracer(attr)
            
        cls.__getatttribute__ = my__getattribute
        return cls
    
    @tracecalls
    class MyClass(object):
        pass

Diving into attribute manipulators
-----------------------------------

The talk dived a bit into things like:

* `__getattribute__`
* `__getattr__`

Diving into this sort of code is tricky, because the reasons for use of these tools is
not necessary in 99% of Python projects. I prefer to rely on `decorators` to alter behavior 
because they are syntactical sugar. Easy to find and very explicit.


relate or !relate
==================

by Mark Ramm

* "*Python has been very good to me*"
* Double major in Philosophy, Literature and minors in Theatre and something else
* Wrote the TurboGears 1 book and became a web developer

Opening
-------

* Tools matter

    * Python is a great tool
    * "SQLAlchemy is the best ORM on the planet regardless of language"
    
* Data matters just as much 

Tools matter
------------

* Know your tools

    * Screws and nails

        * deck (screws are stronger than nails, but harder to use)
        * siding (nailing yourself to the siding)
        * mongodb (nailed the SourceForge team to the wall via MongoDB)

**Takeaway**: If you don't know your tools when you hit production you are going to be trying to debug something critical.

SQL
----

"*Who here has used a non-relational database? Not many? Oh, there's this thing called a FILESYSTEM.*"

ACID
~~~~

    * Atomicity
    * Consistency
    * Independent
    * Durable

Why I NEED relational
~~~~~~~~~~~~~~~~~~~~~

 * I can't use NoSQL because
 
    * It's financial data (need consistency)
    * my data is relational
    
Mark says **BULLSHIT**




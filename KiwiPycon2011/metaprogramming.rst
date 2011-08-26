============================
Metaprogramming Keynote
============================

By jeff Rush


"*Metaprogramming is the programming of programming*"


Make use of
============

    * metaclasses
    * decorators
    * attributes
    * more
  
What is metaprogramming orientation
====================================

  
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

.. sourcecode::

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

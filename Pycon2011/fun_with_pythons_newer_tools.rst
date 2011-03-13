==============================
Fun with Python's new features
==============================

by Raymond Hettiger

**question**: For Collections.counter, I thought you weren't supposed to subclass dicts directly

I think this is all Python 3.x material


Collections.Counter
===================

Can do anything you can do with a dict but you can use counter notation::

    c = Counter()
    c['x'] += 1
    c['y'] += 1    
    del c[x]

Convenience methods:

* most_common(n) returns a sorted list of the n highest counts
* elements() lists all of the contents individually. Differs from __init__ which returns pairs: (elem, count)

Counter Math::

    >>> # simple
    >>> x = Counter(a=1, b=1)
    >>> x.subtract(a=1, c=1)
    >>> x
    Counter({'b':1, 'a':0, 'c':-1})
    >>> #advanced
    >>> {'a','b'} - {'a', 'c'}
    {'b'}
    >>> Counter(a=1,b=1) - Counter(a=1, c=1)
    Counter({'b': 1})

collections.namedtuple()
========================

Works like a regular tuple but lets you assign names to each field:

* makes the code self-documenting
* Makes the printed `__repr__` intelligible
* Lets you change tuple order without affecting client code

One of the single best changes you can make to existing code. The additional space cost for namedtuples is zero

Convenience methods:

* _asdict() turns a named tuple into a dictionary
* _replace() creates a new named tuple with altered values::
    
    >>> result._replace(failed=2)
    TestResult(failed=2, attempted=7)
    
Pro tip: Using the Field Structure::

    >>> LabeledResult = namedtuple(
            LabeledResult,
            TestResult._fields + ('blah'))
            
Pro tip: Every time you make one reset the slots to nothing::

    >>>> class Point(namedtuple):
    ...     __slots__ = ()

caching
=======

LRU Cache::

    from functools import lru_cache
    
    @lru_cahe(maxsize=100)
    def big_computation(*args):
        ...
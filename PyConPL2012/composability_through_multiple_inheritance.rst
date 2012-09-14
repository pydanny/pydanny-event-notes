==========================================
Composability through multiple inheritance
==========================================

Original Polish Title: `Kompozycja poprzez wielokrotne dziedziczenie`

note:: Talk is in English, but title and description were in Polish

* by Łukasz Langa

    * https://twitter.com/llanga
    * TODO: 

Description
============

Jednym z momentów zwrotnych w historii było wprowadzenie produkcji półfabrykatów. Poprzez tworzenie prostych komponentów, które integruje się później w złożone produkty, producenci są w stanie budować szybciej i taniej, osiągając lepszą jakość. W tej opowieści programisty o sercu inżyniera opisuję, jak używam mechanizmu wielokrotnego dziedziczenia dostępnego w Pythonie, by realizować tę rzeczywistość przemysłową w kodzie źródłowym. Przykłady bazują głównie na Django, jego ORM, formularzach i klasowych widokach. Jednakże zasady, które opisuję, są ogólne. W trakcie wykładu wspominam o sposobach implementacji komponowalnych modeli abstrakcyjnych, a także mixinów do formularzy i widoków. Tłumaczę, jak to podejście tworzy czytelne i zarządzalne idiomy, wraz z ich plusami i minusami. Zakończę podsumowując moje doświadczenia z próbą stworzenia biblioteki ściśle reużywalnych komponentów.

This is a talk on composition

Act I: Exposition
====================

* You can use legos to build small things and yet also to build big things.
* Lego blocks do have the composability feature
* To make components work, you need to have a framework that embodies compositionality.
* UNIX pipes are a good example:

.. code-block: bash

    $ ps aux | grep celery | grep -v grep | ...
    
* Composition isn't a science, it's an art    
* Programming done well is art. Programming done badly is trash
* Jamie Zawinksi: You can have a string that describes things accurately, or you can have a string that describes things accurately with flair

.. note:: According to Lucasz, the owner of Lego stole the invention from someone else and patented it, and made a fortune. The actual inventor died of grief.

Act II: Rising Action
======================

* If you use old-style style classes, you're going to have a bad time.

MRO
----

.. code-block:: python

    >>> class A(object):
        pass
    ...
    ...
    >>> A.mro()
    [<class '__main__.A'>, <type 'object'>]
    
Thoughts on the diamond problem
------------------------------------

.. code-block:: python

    >>> class A(object): pass
    >>> class B(object): pass    
    >>> class AB(A,B): pass        
    >>> class BA(B,A): pass     
    >>> class C(D, AB): pass
    >>> class D(A): pass

* Python has a definition of how to resolve the diamond problem in multiple inheritance.

    * Python has cooperative inheritance
    * In our example, you have to carefully watch how things are constructed
    
Super was designed to solve this problem
------------------------------------------

But it failed. It's only useful in limited cases and can fool you.
    
.. code-block:: python

    class D(A):
        def __init__(self):
            super(D, self).__init__(arg_a='d')
            

* Don't omit super(c, self).__init__() even if your base class is `object`
* Don't assume you know what arguments you are going to get
* Dont' assume you know what arguments you should pass to `super`

Warning: If you mix ClassName.__init__() and super your are going to have a bad time.

Django ORM as a diamond pattern case study
------------------------------------------

.. note:: need to cook up proof of this

* Problems: If you have a diamond pattern in Django it causes duplicate fields
* breaks  the Liskov substitution pattern

Act III: Example
=======================

* Use base classes in Django models is a good way to have easily maintained code. Examples:

    * EditorTrackable is a Model base that handles not just who can edit data, but also handles cascading deletes elegantly.
    * TimeTrackable is a model that tracks when something was created/deleted. Includes the following:

        * Created
        * Modified
        * cache_version is an field that tracks which cached version is being displayed

* By composing his models on many projects via Abstract Models, he can test each reused abstract model extensively and repeatedly.

QUESTION to ask: How? Why? The Django ORM fails in the diamond pattern. Even with Abstract base classes?
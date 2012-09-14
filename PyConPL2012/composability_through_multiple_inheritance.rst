==========================================
Composability through multiple inheritance
==========================================

Original Polish Title: Kompozycja poprzez wielokrotne dziedziczenie (talk is in English)

by Łukasz Langa

Description
============

Jednym z momentów zwrotnych w historii było wprowadzenie produkcji półfabrykatów. Poprzez tworzenie prostych komponentów, które integruje się później w złożone produkty, producenci są w stanie budować szybciej i taniej, osiągając lepszą jakość. W tej opowieści programisty o sercu inżyniera opisuję, jak używam mechanizmu wielokrotnego dziedziczenia dostępnego w Pythonie, by realizować tę rzeczywistość przemysłową w kodzie źródłowym. Przykłady bazują głównie na Django, jego ORM, formularzach i klasowych widokach. Jednakże zasady, które opisuję, są ogólne. W trakcie wykładu wspominam o sposobach implementacji komponowalnych modeli abstrakcyjnych, a także mixinów do formularzy i widoków. Tłumaczę, jak to podejście tworzy czytelne i zarządzalne idiomy, wraz z ich plusami i minusami. Zakończę podsumowując moje doświadczenia z próbą stworzenia biblioteki ściśle reużywalnych komponentów.

This is a talk on composition

Act I: Exposition
====================

* You can use legos to build small things and yet also to build big things.
* Lego block do have the composability feature
* To make components work, you need to have a framework that embodies compositionality.
* UNIX pipes are a good example:

.. code-block: bash

    $ ps aux | grep celery | grep -v grep | ...
    
* Composition isn't a science, it's an art    
* Programming done well is art. Programming done badly is trash
* Jamie Zawinksi: You can have a string that describes things accurately, or you can have a string that describes things accurately with flair

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
            

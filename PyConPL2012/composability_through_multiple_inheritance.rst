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

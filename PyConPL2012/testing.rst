============================================
Kompozycja poprzez wielokrotne dziedziczenie
============================================

by Łukasz Langa

.. note:: Started late. And I don't speak Polish. 

Description
============

Jednym z momentów zwrotnych w historii było wprowadzenie produkcji półfabrykatów. Poprzez tworzenie prostych komponentów, które integruje się później w złożone produkty, producenci są w stanie budować szybciej i taniej, osiągając lepszą jakość. W tej opowieści programisty o sercu inżyniera opisuję, jak używam mechanizmu wielokrotnego dziedziczenia dostępnego w Pythonie, by realizować tę rzeczywistość przemysłową w kodzie źródłowym. Przykłady bazują głównie na Django, jego ORM, formularzach i klasowych widokach. Jednakże zasady, które opisuję, są ogólne. W trakcie wykładu wspominam o sposobach implementacji komponowalnych modeli abstrakcyjnych, a także mixinów do formularzy i widoków. Tłumaczę, jak to podejście tworzy czytelne i zarządzalne idiomy, wraz z ich plusami i minusami. Zakończę podsumowując moje doświadczenia z próbą stworzenia biblioteki ściśle reużywalnych komponentów.

This is a talk on continuous integration and best practices.


Pyflakes and PEP-8
==================

* Use tools to validate the quality of your code
* Develop good habits

Coverage.py, nose, and other tools
===================================

* coverage.py lets you know how much is tested
* nose discovers tests.


Automatic Installation
======================

* Create a reproducable installation procedure that is executed via tools
* Don't do it manually

Useful tools include:

* Fabric
* Pip
* Virtualenv

Set up your own QA servers
===========================

* Set up your own servers takes a lot of work and effort.
* OpenStack is nice because:

    * It does a lot of the lifting for you
    * 
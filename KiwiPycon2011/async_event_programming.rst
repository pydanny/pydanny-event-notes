================================================
Asynchronous and Evented programming in Python
================================================

*With Rocks In*

by Aurynn Shaw

* Works at WETA Digital
* https://github.com/aurynn
* She likes shiny things

Not really covering Tornado

Introduction
============

* Much ado about Node.js
* Event driven!
* Tornado, from facebook
* Lots of buzzwords
* Async is '*sort of*' doing two things at once

Threading
==========

Really awesome until you hit issues like:

* Locking
* Shared state is hard
* Even experts have problems with it

Multiprocessing
===============

* Let the kernal care
* Easy to write MP code on unix-likes
* Can even go multi-system

Problems

* Hard to share data
* import multiprocessing can be... quirky
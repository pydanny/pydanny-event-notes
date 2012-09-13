==========================================================
Forms in python - problems and my proposal of solving them
==========================================================

* By Szymon Pyżalski

    * STX Next Python Experts
    * https://github.com/zefciu/Forms-in-python

Talk Description
=================

My lecture would consist of two parts. First I would like to discuss what can a developer expect from a form library. Secondly I will show a design of one that would address all these problems.

Why are they important?
========================

Forms are ubiquitous across all Python frameworks

* Python is a strongly typed language so we have to handle input properly
* Closest to the user 

    * What they see most
    * This is where they tend to see our mistakes
    
* Our first line of defense against security against CSRF and other attack methods.
* Boilerplate and repition removal

Scope of Features
====================

All form libraries need to have the following components:

* User input handling

    * Type coercion
    * Validation
    
* Widget generation
* Data schema reflection
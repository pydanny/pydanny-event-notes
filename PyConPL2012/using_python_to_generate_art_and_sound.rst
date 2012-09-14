======================================
Using Python to Generate Art and Sound
======================================

* by Audrey Roy

    * https://twitter.com/audreyr
    * http://audreymroy.com
    * PSF Member
    * My fiancee!
    
Description
============

I’ve used Python to draw rainbows of different shapes and colors, Gaussian clouds, and landscapes in perspective. I’ve also used Python to create sound effects for games. This talk explores my experiments with the various Python imaging and sound tools. First, I walk the audience through implementing basic audio building blocks with the Python stdlib's wave, math, and array modules. Then, I improve upon the code with NumPy and SciPy. Finally, I demonstrate how audio synthesis can be very similar to generative graphic art, using similar techniques to create building blocks for basic illustration.

background of the Talk
======================

A few years back she was painting landscapes and got tired of repetitive techniques so she decided to write a program to do it for her

Introduction
=============

* Overwhelming variety of Python libraries for audio/graphics
* Understanding the fundamentals first
* Helps you understand your options

Overview
========

* Simple sound with the Python stdlib
* Numpy and Scipy
* Plotting sound arrays with Matplotlib
* Creative sound generation techniques
* Using the same tricks on graphics instead

STDLIB!
=======================

* Very east to get started
* Other libraries can and are tricky to install

Parts she'll be using 

* Wave Module

    * Use it to open and write .vave files
    * Introduced in stdlib 1.6 and hasn't changed much since
    
* Array Module

    * Using it to store data over time

* Math module

    * Using math.sin(x) to calculate 440 Hz audo audio samples
    
wave, array, math
------------------

Generates a 440 Hz sine wave

.. code-block:: python

    import array
    from math import sin, pi
    import wave
    
    SAMPLE_RATE = 44100
    DURATION = 3
    
    # TODO finish
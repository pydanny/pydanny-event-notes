======================================
Using Python to Generate Art and Sound
======================================

* by Audrey Roy

    * https://twitter.com/audreyr
    * http://audreymroy.com
    * PSF Member
    * My fiancee!
    
.. note:: Lots of code samples with detailed explanations. Can't keep up with my notes but it's awesome.
    
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
    
    # TODO finish tons more code
    
Simplifying via a function

.. code-block:: python

    import array
    from math import sin, pi
    import wave

    SAMPLE_RATE = 44100    
    
    def note() # TODO finish coding this out
    
Can this be simplified further?
-------------------------------

* Yes via NumPy arrays!

    * perfect for sound operations
    
.. code-block:: python

    # numpy.linspace(start, stop, num):
    >>> linspace(0, 1, 10)
    array() # TODO get this value
    
    #sumpy.sin(x)

Now we show the simplified example:

.. code-block:: python

    from numpy import linspace, int16, sin
    from scipy.io.wavfile import write  # Using this because it's less code to use than the Wave module
    
    def note(freq, duration, amp=10000, rate=41100):
        # TODO add code stuff here
        pass

Is this music?
---------------

Not yet. You need chords for music!

Chords for music
================

* Simply add 2 notes of different frequencies together
* She looked up Piano key frequencies on wikipedia

.. code-block:: python

    # chord function
    def chord():
        # TODO get a sample of this code
        pass
        
Using matplotlib to visualize the chord
========================================

She showed very nice code to plot out audio files.

Concatenate notes into sequences
===================================

She showed using numpy's `concatenate()` function to add up arrays of sound samples.

Weaving it all together
=========================

File structure

* notes.py

    * contains piano keys
    * contains imports of all the notes components
    
Use numpy's `uniform()` function to create nice distributions of frequencies and durations
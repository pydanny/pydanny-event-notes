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
    
* Used numpy's `uniform()` function to create nice distributions of frequencies and durations

* Constrained the frequencies so they are humanly playable 
* Explained use of random.choice over numpy.choice. Chose it because numpy's version is in beta.

Results
---------

* Colorful rainbow of sounds that sounds relatively pleasant to the ear

Adding Gaussian Distribution
------------------------------------

* Using an algorithm to make things more centralized.
* Which blurred things so instead of a rainbow of sounds it sounded like puffy clouds. :-)

Introducing Pycairo
====================

* Python API for cairo
* HTML Canvas uses cairo as well
* Showed how to use Gaussian algorithm to build clusters of dots

Blocks and Puffs
-------------------

* Show same technique as used in audio to create puffs of clouds
* Added blue background. 
* Alpha and radial gradient background
5. Adjust X and Y axis of gaussian to stretch the clouds into a more cloud-like shape

Not just puffs
---------------

Can also use these processes on colors.

    * Use uniform distribution for picking colors randomly
    * Explore constraining to a subset of colors

* Used this technique and more to generate real paintins

Summary: Think functionally
============================

* Parametize everything
* Use numpy array functions as much as you can
* Can combine wave, array, math from the Python stdlib for audio synthesis
* Sound and art composition are extremely similar
* Experiment with Gaussian distributions

In Memorandum
=============

* John Hunter, founder of Numpy, passed away recently
* http://numfocus.org/johnhunter

Bonus Slide
============

* Tones + filters = sound effects

    * Play with looping, itertools
    
* Image sequences + Reportlab = flipbook PDFs

    * Use strokes and not fills

* Save image + sound sequences as videos
* Image composition can respond to audio input
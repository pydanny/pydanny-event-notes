""" weave_blitz_compare

    This example takes the numpy expression used in the filter_image
    exercise and compares the speed of numpy to that of weave.blitz.
    
    Read in the lena image and use an averging filter
    to "smooth" the image.  Use a "5 point stencil" where
    you average the current pixel with its neighboring pixels

                   0 0 0 0 0 0 0
                   0 0 0 x 0 0 0
                   0 0 x x x 0 0
                   0 0 0 x 0 0 0 
                   0 0 0 0 0 0 0
    
    Once you have a numpy expression that works correctly, time it
    using time.time (or time.clock on windows).
    
    Use scipy.weave.blitz to run the same expression.  Again time it.
    
    Compare the speeds of the two function and calculate the speed-up 
    (numpy_time/weave_time).
    
    Plot two images that result from the two approaches and compare them.
"""

import time
from numpy import empty, float64
from scipy import lena
from scipy import weave
from matplotlib.pylab import subplot, imshow, title, show, gray, figure

img = lena()

expr = """avg_img =(  img[1:-1 ,1:-1]  # center
                    + img[ :-2 ,1:-1]  # left
                    + img[2:   ,1:-1]  # right
                    + img[1:-1 , :-2]  # top
                    + img[1:-1 ,2:  ]  # bottom
                    ) / 5.0"""


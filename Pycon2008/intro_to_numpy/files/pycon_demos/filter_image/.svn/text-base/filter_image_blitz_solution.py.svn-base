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

import time
t1 = time.clock()
for i in range(10):
    exec expr
t2 = time.clock()                         
numpy_time = t2-t1
numpy_avg_img = avg_img

avg_img = empty((img.shape[0]-2, img.shape[1]-2), dtype=float64)

# Run it once so that it gets compiled.
weave.blitz(expr)

import time
t1 = time.clock()
for i in range(10):
    weave.blitz(expr)
t2 = time.clock()                         
blitz_time = t2-t1
blitz_avg_img = avg_img

avg_img = empty((img.shape[0]-2, img.shape[1]-2), dtype=float64)
code = """for (int i=0; i<Navg_img[0];i++)
          { 
            for (int j=0; j<Navg_img[1];j++)  
            {
              AVG_IMG2(i,j) =(  IMG2(i+1 ,j+1)  // center
                              + IMG2(i ,  j+1)  // left
                              + IMG2(i+2, j+1)  // right
                              + IMG2(i+1 ,j  )  // top
                              + IMG2(i+1 ,j+2)  // bottom
                              ) / 5.0;
            }
          }                    
       """

weave.inline(code,['avg_img', 'img'],compiler='gcc')
t1 = time.clock()
for i in range(10):
    weave.inline(code,['avg_img', 'img'],compiler='gcc')
t2 = time.clock()                         
inline_time = t2-t1

inline_avg_img = avg_img

print 'numpy, blitz, speed-up:', numpy_time, blitz_time, numpy_time/blitz_time
print 'numpy, inline, speed-up:', numpy_time, inline_time, numpy_time/inline_time
# Set colormap so that images are plotted in gray scale.
gray()

# Plot the original image first
figure()
subplot(2,3,1)
imshow(numpy_avg_img)
title('numpy filtered image')

# Now the filtered image.
subplot(2,3,2)
imshow(blitz_avg_img)
title('blitz filtered image')

# Now the filtered image.
subplot(2,3,3)
imshow(inline_avg_img)
title('inline filtered image')

# And finally the difference between the two.
subplot(2,3,5)
imshow(numpy_avg_img - blitz_avg_img)
title('blitz difference')    

# And finally the difference between the two.
subplot(2,3,6)
imshow(numpy_avg_img - inline_avg_img)
title('inline difference')    

show()

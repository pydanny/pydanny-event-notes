# Read in the lena image and use an averging filter
# to "smooth" the image.  Use a "5 point stencil" where
# you average the current pixel with its neighboring pixels
#
#               0 0 0 0 0 0 0
#               0 0 0 x 0 0 0
#               0 0 x x x 0 0
#               0 0 0 x 0 0 0 
#               0 0 0 0 0 0 0
#
# Plot the image, the smoothed image, and the difference between the
# two.
#
# Bonus: Re-filter the image by passing the result image
#        through the filter again.  Do this 50 times and plot
#        the resulting image.


from scipy import lena
from matplotlib.pylab import subplot, imshow, title, show, gray, cm

img = lena()
imshow(img, cmap=cm.gray)
show()
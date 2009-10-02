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
from matplotlib.pylab import subplot, imshow, title, show, gray, figure

img = lena()

avg_img =(  img[1:-1 ,1:-1]  # center
          + img[ :-2 ,1:-1]  # top
          + img[2:   ,1:-1]  # bottom
          + img[1:-1 , :-2]  # left
          + img[1:-1 ,2:  ]  # right
         ) / 5.0
                         
                         
# Set colormap so that images are plotted in gray scale.
gray()

# Plot the original image first
subplot(1,3,1)
imshow(img)
title('original')

# Now the filtered image.
subplot(1,3,2)
imshow(avg_img)
title('smooth')

# And finally the difference between the two.
subplot(1,3,3)
imshow(img[1:-1,1:-1] - avg_img)
title('difference')    
show()

# Bonus: Re-filter the image by passing the result image
#        through the filter again.  Do this 50 times and plot
#        the resulting image.

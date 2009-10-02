""" sinc_function
    
    Topics: Broadcasting, Fancy Indexing
    
    Calculate the sinc function, sin(r)/r.  Use a cartesian x,y grid
    and calculate r = sqrt(x**2+y**2) with 0 in the center of the grid.
    Calculate the function for -15,15 for both x and y.
"""    

from numpy import linspace, sin, sqrt
from matplotlib.pylab import imshow, gray, show

x = linspace(-15,15,101)
# flip y up so that it is a "column" vector.
y = linspace(-15,15,101)[:,None]

# because of broadcasting rules, r is 2D.    
r = sqrt(x**2+y**2)    

# calculate our function.
sinc = sin(r)/r

# replace any location where r is 0 with 1.0
sinc[r==0] = 1.0

imshow(sinc, extent=[-15,15,-15,15])
gray()
show()
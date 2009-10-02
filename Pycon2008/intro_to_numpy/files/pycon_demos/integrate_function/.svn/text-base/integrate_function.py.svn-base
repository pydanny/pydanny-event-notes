""" Integrate sin using scipy.integrate.quad.
    Topics: SciPy's integration library, vectorization.

    A. Use scipy.integrate.quad to integrate sin from 
       0 to pi/4.  Print out the result.  
       hint: from scipy import integrate
             integrate.quad?
    
    B. Integrate sin from 0 to x where x is a range of
       values from 0 to 2*pi.  Compare this to the exact
       solution, -cos(x) + cos(0), on a plot.  Also plot
       the error between the two.
       hint: use vectorize so that integrate.quad works
             with arrays as inputs and produces arrays
             as outputs.    
"""
from numpy import linspace, vectorize, sin, cos, pi
from scipy import integrate
from matplotlib.pylab import plot, legend, show, subplot, xlabel, ylabel, \
                             title

# A. integrate sin from 0->2pi

# B. Integrate sin from 0 to x where x is a range of
#    values from 0, 2*pi
x = linspace(0, 2*pi, 101)

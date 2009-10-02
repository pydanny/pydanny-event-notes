""" This example looks at fitting data.
    Note: Adapted from py4science examples.
    
    It has multiple parts:
    
    1. Create a function with exponential decay and plot it.
       
        y = a*exp(-b*x) + c
        
        where a=2.0, b = 0.76, c=0.1

    2. Now add some gaussian noise with 
        mean=0.0 and std=.2
       hint: from numpy.random import normal
             # use normal? to see its documentation.

    3. Calculate 1st, 2nd and 3rd degree polynomial fit to the data.
       hint: from numpy import polyfit, poly1d
   
    4. Bonus: Do a least squares fit to the orignal 
       exponential function using optimize.leastsq.
       Note: If you get to this one, ask for help or
             refer to the solution...
"""
from matplotlib.pylab import figure, plot, title, show, hold, legend, subplot

# 1. Create the signal.
from numpy import exp, linspace


a = 2.0
b = 0.76
c = 0.1
x = linspace(0, 4.0, 1000)


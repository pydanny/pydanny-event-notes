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

def function(x, a, b, c):
    return a*exp(-b*x) + c

y = function(x, a, b, c)

# Plot original data.
#plot(x,y)
#title("Clean signal")
#show()

# 2. Now add some noise.
from numpy.random import normal

noisy_y = y + normal(0,.1,size=y.shape)

subplot(1,3,1)
plot(x,noisy_y,label="Noisy")
plot(x,y,label="Clean",linewidth=2)
title("%3.2fexp(-%3.2fx)+%3.2f" % (a,b,c))
legend()

# 3. polynomial fit for 1st, 2nd, and 3rd degree.
from numpy import polyfit, poly1d

subplot(1,3,2)
plot(x,noisy_y)
hold('on')
for deg in [1,2,3]:
    coef = polyfit(x, noisy_y, deg)
    poly = poly1d(coef)
    poly_y = poly(x)
    plot(x, poly_y,
         linewidth=2,
         label="order=%d" % deg)
title("Polynomial Fit")
legend()
show()

# 4. Use numpy.leastsq to fit the actual function.
from scipy.optimize import leastsq

def error_func(guess, x, data, function):
    return data - function(x, *guess)
        
best, msg = leastsq(error_func, x0=[0.0, 0.0, 0.0], 
                    args=(x,noisy_y,function))        
                    
leastsq_y = function(x,*best)

subplot(1,3,3)
plot(x,y, 'b', label="Actual", lw=5)
label=r"$%3.2fe^{-%3.2fx}+%3.2f$" % tuple(best)
plot(x,leastsq_y, 'r', label=label, lw=2) 
title("Exponential Fit")
legend()
show()
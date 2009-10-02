Numerics and Python
-------------------
       
    1. calc_derivative
       Topics: NumPy arrays indexing and math.
       
       Caluculate the numerical derivative of sin from 0-2*pi.
       Plot the resulting values and compare to cos.
    
       Bonus points: Implement integration of the same function
                     using reimann sums or the trapazoidal rule.
    
       Here is a helpful starting point:
       
        from numpy import linspace, pi, sin, cos, cumsum
        from matplotlib.pylab import plot, show, subplot, legend, title
        
        # calculate the sin() function on evenly spaced data.
        x = linspace(0,2*pi,101)
        y = sin(x)
    
    2. filter_image
       Topics: Multi-dimensional array indexing and math.
       
       Read in the lena image and use an averging filter
       to "smooth" the image.  Use a "5 point stencil" where
       you average the current pixel with its neighboring pixels
    
                   0 0 0 0 0 0 0
                   0 0 0 x 0 0 0
                   0 0 x x x 0 0
                   0 0 0 x 0 0 0 
                   0 0 0 0 0 0 0
    
       Plot the image, the smoothed image, and the difference between the
       two.
        
       Here is a reasonable starting point.
       
        from scipy import lena
        from matplotlib.pylab import subplot, imshow, title, show, gray
        
        img = lena()
    
    3. sinc_function
       Topics: Numpy array broadcasting and math.
       
       Calculate the sinc function, sin(r)/r.  Use a cartesian x,y grid
       and calculate r = sqrt(x**2+y**2) with 0 in the center of the grid.
       Calculate the function for -15,15 for both x and y.
    
        from numpy import linspace, sin, sqrt
        from matplotlib.pylab import imshow, gray, show   

    4. structured_array

       1. Read all the logs out of a file and into a "structured" array.
       2. Write a routine that will remove a "row" of the array if any
          of the fields for that row are NULL (-999.25).
       3. plot the VP vs VS logs.

    5. Data fitting
       Topics: polynomials, noise, leastsq
        
        This example looks at fitting data.
        
        It has multiple parts:
        
        a. Create a set of function with exponential decay
           and plot it.
           
            y = a*exp(-b*x) + c
            
            where a=2.0, b = 0.76, c=0.1
    
        b. Now add some gaussian noise with 
            mean=0.0 and std=.2
           hint: from numpy.random import normal
                 # use normal? to see its documentation.
    
        c. Calculate 1sr, 2nd and 3rd degree polynomial fit to the data.
           hint: from numpy import polyfit, poly1d
       
        d. Bonus: Do a least squares fit to the orignal 
           exponential function using optimize.leastsq.
           Note: If you get to this one, ask for help or
                 refer to the solution...

    6. integrate_function
       Topics: SciPy's integration library, vectorization.
    
       Integrate sin using scipy.integrate.quad.

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

Interfacing with other languages
--------------------------------
            
    1. weave_compare
       Topics: weave.blitz and weave.inline        
       
       Compare the speed of numpy, weave.blitz and weave.inline
       for the following equation:
    
        result=a+b*(c-d)
    
       Set up all arrays so that they are 1 dimensional and have 1 million 
       element in them.

    2. blitz_inline_compare
       Topics: weave.blitz and weave.inline        
       
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

    3. f2py_fcopy
       Topics: f2py
       
       In this example we'll use f2py to wrap a simple fortran function
       found in fcopy.f so that it can be called by python.  The file
       already has a working version of the wrapper.  Your job is to
       improve the wrapper so that it is more pythonic.  The example
       follows along exactly with the notes from the lecture.

       See the readme.txt file in the f2py_fcopy directory for more
       information.

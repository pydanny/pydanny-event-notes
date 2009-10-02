""" structured_array

    1. Read all the logs out of a file and into 1D array.
    2. Create a "structured array" view of this 1D data that has
       a field for each log.
    3. Create a mask for the "good" values in the array that
       will mask a "row" of the array if *any* of the measured logs
       have a NULL value (-999.25).
       hint: It is easier to do this with a 2D "view" of the array.
             The alltrue function is also useful here.
       
       Also, replace all -999.25 values with NaNs.             
    4. plot the VP vs VS logs.
    5. compare nansum and sum on both of these logs.    
"""
from pylab import plot, show
import numpy

# Open the file.
log_file = open('data.dat')

# The first line is a header that has all the log names.
header = log_file.readline()
log_names = header.split()

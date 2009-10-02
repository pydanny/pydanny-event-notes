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
from pylab import plot, show, hold
import numpy

# 1. and 2.
# Open the file.
log_file = open('data.dat')

# The first line is a header that has all the log names.
header = log_file.readline()
log_names = header.split()

# Construct the array "dtype" that describes the data.  All fields
# are 8 byte (64 bit) floating point.
fields = zip(log_names, ['f8']*len(log_names))
#fields = [(name, 'f8') for name in log_names]
fields_dtype = numpy.dtype(fields)
        
# Now, read in all of the data in one fail swoop, translating
# it into floating point values as we go.  Use the dtype 
# we created above so that the logs can be addressed by index or field.
value_text = log_file.read()
lst = [float(val) for val in value_text.split()]
values = numpy.array(lst)
logs = values.view(fields_dtype)

values.shape = len(values)/len(fields), len(fields)

# 3.
# Use the "2D array" view of logs to find any log samples
# with missing values (-999.25).  We'll use this mask
# to pull out the samples that don't have *any* missing values.
data_mask = numpy.alltrue(values!=-999.25, axis=-1)
good_logs = logs[data_mask]

# Create a 2nd log with all the missing values removed.

# Also, mark all NULL values with NaNs in the orginal log for good measure.
values[values==-999.25] = numpy.NaN

# 4.
# Plotting will ignore NaNs, so this looks the same as plotting
# good logs.
plot(good_logs['VP'], good_logs['VS'], 'o')
hold(True)
plot(logs['VP'], logs['VS'], '+')
show()   

# 5.
# However, not all calculations.  sum(), mean(), etc. do not 
# ignore nans.  There are some functions that do (nansum(), etc.)
# Note that nansum values are different than sum because
# not all the VP values that are non-nan are in the good_logs.
print 'sum good_logs:', numpy.sum(good_logs['VP'])
print 'sum of logs:', numpy.sum(logs['VP'])
print 'nansum of logs:', numpy.nansum(logs['VP'])
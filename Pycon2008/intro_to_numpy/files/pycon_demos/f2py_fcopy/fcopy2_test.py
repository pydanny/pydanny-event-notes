from numpy import array, complex64, alltrue

import fcopy2

a = array((1.0+1j, 2.0, 3.0),dtype=complex64)
b = fcopy2.fcopy(a)

print 'a==b:', alltrue(a==b)
print "a:", a
print "b:", b
print b.dtype
from numpy import array, complex128, zeros, alltrue

import fcopy

a = array((1.0+1j, 2.0, 3.0),dtype=complex128)
b = zeros(3,dtype=complex128)
fcopy.fcopy(a,len(a),b)

print 'a==b:', alltrue(a==b)
print "a:", a
print "b:", b
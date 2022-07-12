import time
t1 = time.clock()

import math

def isSqr(x):
    return math.sqrt(x)**2 == x

N = 10**6
m = .5*N

s = 0
for b in xrange(1, m/2):
    for c in xrange(b, m/2):
        a = ((2*b)**2+1)*((2*c)**2+1)-1
        x = math.sqrt(a)
        if int(x) == x:
            s += x/2

print s

t2 = time.clock()
print 'Time elapsed: ', t2-t1

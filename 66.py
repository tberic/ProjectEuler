import math
import time
t1 = time.clock()

def minsol(x):
    m = 0
    d = 1
    a = int(math.floor(math.sqrt(x)))

    h0, h1 = 1, a
    k0, k1 = 0, 1
    
    while True:
        m = int(d*a - m)
        d = int((x - m**2)/d)
        a = int(math.floor( float(math.sqrt(x) + m)/d ))

        h1, h0 = a*h1 + h0, h1
        k1, k0 = a*k1 + k0, k1

        if h1**2 - x*k1**2 == 1:
            break
        
    return h1

max = 0
for i in range(2, 1001):
    a = int(math.sqrt(i))
    if a*a < i:
        t = minsol(i)
        if t > max:
            max = t
            maxi = i

print maxi

t2 = time.clock()
print 'Elapsed time: ', t2-t1

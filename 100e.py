import math
import time
t1 = time.clock()

n = 183648021599
b = int((1 + math.sqrt(2*n**2 - 2*n + 1))/2)
sn = n*(n-1)
sb = 2*b*(b-1)

while sn != sb:
    if sb > sn:
        b -= 1
        sb -= 4*b
    else:
        n -= 1
        sn -= 2*n

print b, n

t2 = time.clock()
print 'Elapsed time: ', t2-t1

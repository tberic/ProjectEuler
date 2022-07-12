import math
import time
t1 = time.clock()

n = 2
b = 2
sn = n*(n-1)
sb = 2*b*(b-1)

while n < 10**12:
    while sn != sb:
        if sb < sn:
            sb += 4*b
            b += 1
        else:
            sn += 2*n
            n += 1
    print b, n
    sn += 2*n
    n += 1

t2 = time.clock()
print 'Elapsed time: ', t2-t1

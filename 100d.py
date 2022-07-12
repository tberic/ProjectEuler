import math
import time
t1 = time.clock()

n = 5
b = 2
sn = n*(n-1)
sb = 2*b*(b-1)

sol = [4]

while n < 10**12:
    while sn != sb:
        if sb < sn:
            sb += 4*b
            b += 1
        else:
            sn += 2*n
            n += 1
    print b, n
    sol.append(n)
    n = int(float(sol[-1])/sol[-2]*n)
    sn = n*(n-1)
    b = int((1 + math.sqrt(2*n**2 - 2*n + 1))/2)
    sb = 2*b*(b-1)

t2 = time.clock()
print 'Elapsed time: ', t2-t1

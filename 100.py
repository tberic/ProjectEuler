import math
import time
t1 = time.clock()

N = 10**12

n = N
b = (n-1)**2
while True:
    b += n**2
    a = math.sqrt( b )
    if a*a == b:
        break
    b -= (n-1)**2
    n += 1

print n, (int(a)+1)/2

t2 = time.clock()
print 'Elapsed time: ', t2-t1

import math
import time
t1 = time.clock()

N = 10**12

b = int( (1 + math.sqrt( (N-1)**2 + N**2 ))/2. )
while True:
    n = (1 + math.sqrt( 1 + 8*b*(b-1) ))/2.
    if n == int(n):
        break
    b += 1

print int(n), b

t2 = time.clock()
print 'Elapsed time: ', t2-t1

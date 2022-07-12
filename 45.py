import math
import time
t1 = time.clock()

def H(n):
    return n*(2*n-1)

m = 144
while True:
    a = math.sqrt(48*m*m - 24*m + 1)
    if a == int(a) and a % 6 == 5:
        break    
    m += 1
    
print H(m)

t2 = time.clock()
print 'Elapsed time: ', t2-t1

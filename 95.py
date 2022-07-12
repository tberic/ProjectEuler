import math
import time
t1 = time.clock()

def sumdiv(x):
    a = int(math.sqrt(x))
    s = 1
    for i in range(2, a):
        if (x % i == 0):
            s += i
            s += x/i
    if (a*a == x):
        s += a
    return s
    






t2 = time.clock()
print 'Elapsed time: ', t2-t1

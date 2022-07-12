import math
import time
t1 = time.clock()

def issquare(x):
    a = int(math.sqrt(x))
    return a*a == x






t2 = time.clock()
print 'Elapsed time: ', t2-t1

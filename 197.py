import time
import math
t1 = time.clock()

a = 30.403243784

def f(x):
    return float(int(2**(a-x*x)))/(10**9)

N = 1000

u = -1
for i in range(N):
    #print u
    u = f(u)

print u + f(u)

t2 = time.clock()
print 'Elapsed time: ', t2-t1

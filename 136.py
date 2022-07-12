#not good
import math
import time
t1 = time.clock()

def isprime(x):
    if x == 1:
        return 0
    if x in [2, 3, 5, 7]:
        return 1
    if x % 2 == 0 or x % 3 == 0 or x % 5 == 0 or x % 7 == 0:
        return 0
    if x % 6 != 1 and x % 6 != 5:
        return 0
    j = 9
    while (j*j <= x):
        if (x % j == 0):
            return 0
        j += 2
    return 1

N = 50*10**6
n = int(N/8)

p = [2, 3, 5, 7]
for i in range(11, n+1, 2):
    if isprime(i):
        p.append(i)

np = len(p)
print np**2



t2 = time.clock()
print 'Elapsed time: ', t2-t1

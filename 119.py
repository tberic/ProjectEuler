import math
import time
t1 = time.clock()

def sumdigits(x):
    s = 0
    while (x > 0):
        s += x%10
        x /= 10
    return s

N = 15

b = []
e = []

for s in range(2, 9*(N-1)+1):
    k = 2
    while (s**k < 10**N):
        if sumdigits(s**k) == s:
            b.append(s)
            e.append(k)
        k += 1

#sort (optional), I can also guess the largest number

print len(b)

t2 = time.clock()
print 'Elapsed time: ', t2-t1

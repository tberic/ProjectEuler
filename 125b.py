import math
import time
t1 = time.clock()

def isPalin(x):
    s = str(x)
    return s == s[::-1]

found = set()

N = 10**8

for i in range(1, int(math.sqrt(N))):
    t = i*i
    for j in range(i+1, int(math.sqrt(N))):
        t += j*j
        if t >= N:
            break
        if isPalin(t):
            found.add(t)
            
sum = 0
for x in found:
    sum += x
print sum

t2 = time.clock()
print 'Elapsed time: ', t2-t1

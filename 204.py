import math
import time
t1 = time.clock()

def isprime(x):
    i = 2
    while i*i <= x:
        if x % i == 0:
            return 0
        i += 1
    return 1

p = []
N = 100
for i in range(2, N+1):
    if isprime(i):
        p.append(i)
n = len(p)
k = [0 for i in range(n+1)]
k[n] = 10**10

def sumlog():
    s = 0
    for i in range(n):
        s += k[i]*math.log(p[i], 10)
    return s

def num():
    s = 1
    for i in range(n):
        s *= p[i]**k[i]
    return s


cnt = 0

while True:
    for i in range(n+1):
        k[i] += 1
        if sumlog() <= 9:
            cnt += 1
            #print num()
            break
        k[i] = 0
    if i == n:
        break

print cnt

t2 = time.clock()
print 'Elapsed time: ', t2-t1

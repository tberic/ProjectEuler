import math
import time
t1 = time.clock()

N = 4*(2*10**6)
x = int(math.sqrt(N))

min = N
m = 0
while (m*(m+1)*2 < N):
    m += 1
    n = int(math.sqrt( N/(m*(m+1)) ))
    while (m*(m+1)*n*(n+1) < N):
        n += 1
    if abs(m*(m+1)*n*(n+1) - N) < min:
        min = abs(m*(m+1)*n*(n+1) - N)
        mina = m
        minb = n
    if abs(m*(m+1)*(n-1)*n - N) < min:
        min = abs(m*(m+1)*(n-1)*n - N)
        mina = m
        minb = n-1

print mina, minb

t2 = time.clock()
print 'Elapsed time: ', t2-t1

#approx 3 minutes
import time
t1 = time.clock()

def repunitmod(n, p):
    n = n % (p-1)
    if (n == 0):
        return 0

    k = 1
    m = 1
    d = 1
    while (k < n):
        k = k + 1
        d = (d*10) % p
        m = (m + d) % p
    return m

N = 10**6

#first find primes
p = [1 for i in range(N)]
for i in range(2, N):
    if (p[i] == 1):
        j = 2
        while (j*i < N):
            p[j*i] = 0
            j += 1

M = 10**9
np = 40

s = 0
t = 0
for i in range(7, N, 2):
    if (p[i] and repunitmod(M, i) == 0):
        t = t + 1
        s = s + i
        print i
        if (t == np):
            break

print s

t2 = time.clock()
print 'Elapsed time: ', t2-t1

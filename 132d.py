#slightly faster than 132c
#the slowest part is the sieve
import time
t1 = time.clock()

def sqr(x):
    return x*x

def bigmod(b, p, m):
    if (p == 0):
        return 1
    if (p%2 == 0):
        return sqr(bigmod(b, p/2, m)) % m
    else:
        return ( (b%m) * bigmod(b, p-1, m) ) % m

def gcd(a, b):
    if (b == 0):
        return a
    return gcd(b, a%b)

def repunitmod(n, p):
    n = gcd(n, p-1)
    return bigmod(10, n, p)

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
    if (p[i] and repunitmod(1000000000, i) == 1):
        t = t + 1
        s = s + i
        print i
        if (t == np):
            break

print s

t2 = time.clock()
print 'Elapsed time: ', t2-t1

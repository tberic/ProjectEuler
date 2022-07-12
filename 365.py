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

np = 5000
#sieve
prime = [1 for i in range(np)]
prime[0] = 0
prime[1] = 0
for i in range(2, np):
    j = 2
    while (i*j < np):
        prime[i*j] = 0
        j += 1

N = 9
s = 0
for p in range(1001, 5000):
    if prime[p]:
        for q in range(p+1, 5000):
            if prime[q]:
                for r in range(q+1, 5000):
                    if prime[r]:
                        a = bigmod(10, 2*N, p)*bigmod(10, 2*N, q)*bigmod(10, 2*N, r)
                        b = bigmod(10, N, p)*bigmod(10, N, q)*bigmod(10, N, r)
                        s += (a*b) % (p*q*r)
                        
print s

t2 = time.clock()
print 'Elapsed time: ', t2-t1

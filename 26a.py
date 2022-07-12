import time

n = 1000

def cycle(d):
    res = [0 for i in range(d)]
    a = 1

    i = 0
    while (res[a%d] == 0 and a % d != 0):
        i += 1
        if (a < d):
            a *= 10
        else:
            res[a % d] = i
            a = (a % d)*10

    if (a % d == 0):
        return 0

    return i - res[a%d] + 1

t1 = time.clock()

#first find primes
p = [1 for i in range(n)]
for i in range(2, n):
    if (p[i] == 1):
        for j in range(2, n/i):
            p[j*i] = 0
    

max = 0
for d in range(2, n):
    if (p[d] and cycle(d) > max):
        max = cycle(d)
        maxi = d

t2 = time.clock()

print maxi
print 'Time elapsed: ', t2-t1


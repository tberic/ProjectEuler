import time

n = 1000
N = 10**6

t1 = time.clock()

#first find primes
p = [1 for i in range(N)]
for i in range(2, N):
    if (p[i] == 1):
        for j in range(2, N/i):
            p[j*i] = 0
    
max = 0
for b in range(2, n):
    if p[b]:
        for a in range(-n+1, n):
            t = 0
            while (p[t*t + a*t + b]):
                t += 1
            if t > max:
                max = t
                maxa = a
                maxb = b
                
print maxa, maxb, max

t2 = time.clock()
print 'Time elapsed: ', t2-t1


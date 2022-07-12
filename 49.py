import time

def digits(a, b):
    da = [a%10, (a/10)%10, (a/100)%10, a/1000]
    db = [b%10, (b/10)%10, (b/100)%10, b/1000]

    da.sort()
    db.sort()

    return da == db

t1 = time.clock()

N = 10**4

#first find primes
p = [1 for i in range(N)]
for i in range(2, N):
    if (p[i] == 1):
        j = 2
        while (j*i < N):
            p[j*i] = 0
            j += 1
    
q = [0 for i in range(1061)]
nq = 0
for i in range(1000, 10000):
    if p[i]:
        q[nq]= i
        nq += 1

for i in range(nq):
    for j in range(i+1, nq):
        if digits(q[i], q[j]):
            for k in range(j+1, nq):
                if (q[k]-q[j] == q[j]-q[i] and digits(q[j], q[k])):
                    print q[i], q[j], q[k]


t2 = time.clock()
print 'Time elapsed: ', t2-t1


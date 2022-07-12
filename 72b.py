import math
import time
t1 = time.clock()

N = 10**6
sieveLimit = int(math.sqrt(N))
spf = [ (2 if i%2==0 else i) for i in range(N+1)]

for i in range(3, sieveLimit+1, 2):
    if spf[i] == i:
        j = i
        while (j*i <= N):
            if spf[i*j] == i*j:
                spf[i*j] = i
            j += 2

phi = [0 for i in range(N+1)]

for i in range(2, N+1):
    if spf[i] == i:
        phi[i] = i-1
    else:
        p = spf[i]
        m = i / p
        if spf[m] == p:
            factor = p
        else:
            factor = p-1
        phi[i] = factor*phi[m]

print sum(phi[2:])

t2 = time.clock()
print 'Elapsed time: ', t2-t1

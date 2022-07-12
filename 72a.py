import time
t1 = time.clock()

N = 10**6
phi = [i for i in range(N+1)]

for i in range(2, N+1):
    if phi[i] == i:
        j = 1
        while (i*j <= N):
            phi[j*i] -= phi[j*i] / i
            j += 1

print sum(phi[2:])

t2 = time.clock()
print 'Elapsed time: ', t2-t1

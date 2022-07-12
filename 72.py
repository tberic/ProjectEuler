#incorrect phi generation
import time
t1 = time.clock()

N = 10**6
phi = [1 for i in range(N+1)]
p = [1 for i in range(N+1)]

p[0] = 0
p[1] = 0
for i in range(2, N):
    j = 2
    if p[i]:
        phi[i] = i-1
        while (i*j <= N):
            p[j*i] = 0
            j += 1

print phi[1:13]

for i in range(2, N):
    if p[i]:
        j = i*i
        k = 2
        while j <= N:
            phi[j] = i**(k-1)*phi[i]
            j *= i
            k += 1

print phi[1:13]

for i in range(2, N):
    j = 2
    while (j <= i and i*j <= N):
        if phi[i*j] == 1:
            phi[j*i] = phi[j]*phi[i]
        j += 1

print sum(phi[2:])

t2 = time.clock()
print 'Elapsed time: ', t2-t1

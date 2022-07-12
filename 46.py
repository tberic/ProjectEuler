import time
t1 = time.clock()

N = 10**5
p = [1 for i in range(N)]
#sieve
for i in range(2, N):
    j = 2
    while (j < N/i):
        p[i*j] = 0
        j += 1

a = [0 for i in range(N)]
#another sieve
for i in range(2, N):
    if p[i]:
        j = 1
        while (i + 2*j**2 < N):
            a[i + 2*j**2] = 1
            j += 1

for i in range(3, N, 2):
    if p[i] == 0 and a[i] == 0:
        print i
        break

t2 = time.clock()
print 'Elapsed time: ', t2-t1

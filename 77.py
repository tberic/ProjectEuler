import math
import time
t1 = time.clock()

def isprime(x):
    if x == 1:
        return 0
    if x in [2, 3, 5, 7]:
        return 1
    if x % 2 == 0 or x % 3 == 0 or x % 5 == 0 or x % 7 == 0:
        return 0
    if x % 6 != 1 and x % 6 != 5:
        return 0
    j = 9
    while (j*j <= x):
        if (x % j == 0):
            return 0
        j += 2
    return 1

NP = 10**2
p = []
for i in range(NP):
    if isprime(i):
        p.append(i)

N = 10**4
a = [[0 for j in range(NP+1)] for i in range(N+1)]
a[2][p[0]] = 1
a[3][p[1]] = 1

for n in range(4, N):
    for i in range(len(p)-1, -1, -1):
        if n == p[i]:
            a[n][p[i]] = 1
        if n > p[i]:
            a[n][p[i]] = a[n][p[i+1]] + a[n-p[i]][p[i]]
    if a[n][p[0]] >= 5000:
        break

print n

t2 = time.clock()
print 'Elapsed time: ', t2-t1

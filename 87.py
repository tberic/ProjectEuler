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

N = 50*10**6
c = math.sqrt(math.sqrt(N))
b = math.pow(N, 1./3)
a = math.sqrt(N)

p = []

na = 0
nb = 0
nc = 0
for i in range(2, a+1):
    if isprime(i):
        p.append(i)
        if i <= b:
            nb += 1
        if i <= c:
            nc += 1
        na += 1

scf = {}

cnt = 0
for x in range(na):
    for y in range(nb):
        for z in range(nc):
            t = p[x]**2 + p[y]**3 + p[z]**4
            if t <= N:
                if t not in scf:
                    cnt += 1
                    scf[t] = 1
            else:
                break

print cnt

t2 = time.clock()
print 'Elapsed time: ', t2-t1

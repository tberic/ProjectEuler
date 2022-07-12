import time
t1 = time.clock()

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a%b)

N = 12000
frac = []

for d in range(2, N+1):
    for n in range(1, d):
        if gcd(n, d) == 1:
            frac.append(float(n)/d)

frac.sort()
i = 0
while frac[i] < 1./3:
    i += 1
i += 1

cnt = 0
while frac[i] < 1./2:
    cnt += 1
    i += 1

print cnt

t2 = time.clock()
print 'Elapsed time: ', t2-t1

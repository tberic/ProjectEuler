import time
t1 = time.clock()

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a%b)

N = 12000

cnt = 0
for d in range(5, N+1):
    for n in range(d/3+1, (d-1)/2+1):
        if gcd(n, d) == 1:
            cnt += 1

print cnt

t2 = time.clock()
print 'Elapsed time: ', t2-t1

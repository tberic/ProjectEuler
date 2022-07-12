import time
t1 = time.clock()

def sumsqrdig(x):
    s = 0
    while (x > 0):
        s += (x%10)**2
        x /= 10
    return s

def chain89(x):
    if (x == 89):
        return 1
    if (x == 1):
        return 0
    return chain89(sumsqrdig(x))

N = 7
c = [0 for i in range(N*9**2+1)]
for i in range(1, N*9**2+1):
    c[i] = chain89(i)

cnt = 0
for i in range(1, 10**N):
    if c[sumsqrdig(i)]:
        cnt += 1

print cnt

t2 = time.clock()
print 'Elapsed time: ', t2-t1

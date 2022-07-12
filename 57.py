import time
t1 = time.clock()

def gcd(a, b):
    if (b == 0):
        return a
    return gcd(b, a%b)

def expansion(N):
    a = 1
    b = 0

    for k in range(N, 1, -1):
        b, a = a, b
        a = a + 2*b

    b, a = a, b
    a = a + b

    #a /= gcd(a,b)
    #b /= gcd(a,b)

    #print a, b

    return len(str(a)) > len(str(b))

cnt = 0
for n in range(1, 1001):
    if expansion(n+1):
        cnt += 1

print cnt

t2 = time.clock()
print 'Elapsed time: ', t2-t1

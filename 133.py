import math

def factor(x):
    factors = {}
    for p in range(2, int(math.sqrt(x)+1)):
        i = 0
        while x % p == 0:
            x //= p
            i += 1
        if i:
            factors[p] = i
    if x > 1:
        factors[x] = 1
    return factors

def a(n):
    x = n
    for k in factor(n):
        x = x // k * (k - 1)
    for k in factor(x):
        while x % k == 0 and pow(10, x // k, n) == 1:
            x //= k
    return x

def fac25(x):
    while (x % 2 == 0):
        x /= 2
    while (x % 5 == 0):
        x /= 5
    return (x == 1)

N = 10**5
#sieve
p = [1 for i in range(N)]
for i in range(2, N):
    if (p[i] == 1):
        j = 2
        while (j*i < N):
            p[j*i] = 0
            j += 1

s = 2+3+5+7
for i in range(2, (N-1)/6):
    if (6*i-1) % 3 and p[6*i-1]:
        if fac25(a(6*i-1)):
            print 6*i-1
        else:
            s += 6*i-1
    if (6*i+1) % 3 and p[6*i+1]:
        if fac25(a(6*i+1)):
            print 6*i+1
        else:
            s += 6*i+1
#    if p[6*i-1] and fac25(a(6*i-1)):
#        print 6*i-1
#    if p[6*i+1] and fac25(a(6*i+1)):
#        print 6*i+1

print s

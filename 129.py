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

for i in range(10**6+1, 10**7, 2):
    if i % 3 and i % 5 and a(i) > 10**6:
        break
print i

for j in range(10**6+2, i, 3):
    k = j
    t = 1
    while (k % 3 == 0):
        k = k / 3
        t *= 3
    if a(k) % 3:
        t = 3*a(k)
    if (t > 10**6):
        break
print j

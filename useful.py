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

def ispandigital(x):
    d = [0 for i in range(10)]
    d[0] = 1
    while (x > 0):
        if d[x%10]:
            return 0
        d[x%10] = 1
        x = x / 10
    return sum(d) == 10

def ispalindrome(x):
    s = str(x)
    n = len(s)
    i = 0
    while s[i] == s[n-i-1] and i < n/2:
        i += 1
    return i == n/2

def reverse(x):
    s = 0
    while (x > 0):
        s = s*10 + (x%10)
        x /= 10
    return s

#sieve
p = [1 for i in range(N)]
p[0] = 0
p[1] = 0
for i in range(2, N):
    j = 2
    while (i*j < N):
        p[j*i] = 0
        j += 1

def EulerPhi(x):
    t = x
    if (x % 2 == 0):
        t /= 2
        while (x % 2 == 0):
            x /= 2
    i = 3
    while (x > 1):
        if (x % i == 0):
            t /= i
            t *= (i-1)
            while (x % i == 0):
                x /= i
        i += 2
    return t

def gcd(a, b):
    if (b == 0):
        return a
    return gcd(b, a%b)

def powermod(a, b, n):
    x = a
    y = 1
    while (b > 0):
        if (b % 2 == 1):
            y = y*x % n
        x = x*x % n
        b = b / 2
    return y

def bigmod(b, p, m):
    if (p == 0):
        return 1
    if (p%2 == 0):
        return sqr(bigmod(b, p/2, m)) % m
    else:
        return ( (b%m) * bigmod(b, p-1, m) ) % m

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

#arbitrarily nested loops
while True:
    for i in range(n+1):
        k[i] += 1
        if k[i] < limit[i]:
            do_something()
            break
        k[i] = 0
    if i == n:
        break

#permutacije
from itertools import permutations
concat = ''.join
list(map(concat, permutations('123456789')))


#reading a file
f = open('59.txt')
for l in f:
	a = [int(x) for x in l.split(',')]
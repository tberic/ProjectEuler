import time
t1 = time.clock()

def isprime(x):
    if x == 1:
        return False
    if x in [2, 3, 5, 7, 11]:
        return True
    if (x % 2 == 0 or x % 3 == 0 or x % 5 == 0 or x % 7 == 0 or x % 11 == 0):
        return False
    i = 13
    while i*i <= x:
        if x % i == 0:
            return False
        i += 2
    return True

def replace(x, k, d):
    s = list(str(x))
    for i in range(len(k)):
        if k[i] == '1':
            s[i] = str(d)

    s = ''.join(s)
    return int(s)

def samedig(x, k):
    s = list(str(x))
    t = -1
    for i in range(len(k)):
        if k[i] == '1':
            if t == -1:
                t = int(s[i])
            elif t != int(s[i]):
                return False

    return True


n = 6
N = 10**n
m = 8

p = [1 for i in range(N)]
for i in range(2, N):
    j = 2
    while (i*j < N):
        p[i*j] = 0
        j += 1

max = 0
for i in range(10**(n-1)+1, 10**n, 2):
    if p[i]:
        for k in range(2, 2**n-1, 2):
            if samedig(i, '0'*(n-len(bin(k))+2) + bin(k)[2:]):
                t = 0
                for d in range(10):
                    if p[replace(i, '0'*(n-len(bin(k))+2) + bin(k)[2:], d)]:
                        t += 1
                if t == m:
                    print i, k

t2 = time.clock()
print 'Elapsed time: ', t2-t1

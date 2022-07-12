import time
t1 = time.clock()

def concat(x, y):
    d = []
    while y > 0:
        d.append(y%10)
        y /= 10
    for i in range(len(d)-1, -1, -1):
        x = x*10 + d[i]
    return x

def isprime(x):
    if x in [2, 3, 5, 7, 11, 13]:
        return True
    if x % 2 == 0 or x % 3 == 0 or x % 5 == 0 or x % 7 == 0 \
        or x % 11 == 0 or x % 13 == 0:
            return False
    i = 17
    while i*i <= x:
        if x % i == 0:
            return False
        i += 2
    return True

def over(x):
    for i in range(n):
        if not isprime(concat(p[i], x)) or not isprime(concat(x, p[i])):
            return False
    return True

n = 4
p = [3, 7, 109, 673]

i = p[n-1]/6+1
while True:
    if isprime(6*i-1):
        if over(6*i-1):
            print sum(p[:n])+6*i-1
            break
    if isprime(6*i+1):
        if over(6*i+1):
            print sum(p[:n])+6*i+1
            break
    i += 1

t2 = time.clock()
print 'Elapsed time: ', t2-t1

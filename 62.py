import math
import time
t1 = time.clock()

def digits(x):
    dig = []
    while x > 0:
        dig.append(x%10)
        x /= 10
    dig.sort()
    return dig

n = 1
while True:
    n += 1
    a = math.ceil(math.pow(10**(n-1), 1./3))
    b = math.floor(math.pow(10**n, 1./3))

    c = []
    for i in range(a, b+1):
        c.append(i**3)

    for i in range(len(c)):
        t = 0
        for j in range(i+1, len(c)):
            if digits(c[i]) == digits(c[j]):
                t += 1
        if t == 4:
            x = c[i]
            break

    if t == 4:
        break

print x

t2 = time.clock()
print 'Elapsed time: ', t2-t1

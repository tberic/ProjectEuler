import time
t1 = time.clock()

def isprime(x):
    if (x == 1 or x == 4 or x == 6):
        return 0
    if (x == 2 or x == 3 or x == 5 or x == 7):
        return 1
    if (x % 2 == 0):
        return 0
    i = 3
    while (i*i <= x):
        if (x % i == 0):
            return 0
        i += 2
    return 1


p = 3
a = 3
while (10*p > 2*a-1):
    #print p, a, float(p)/(2*a-1)

    a += 2
    if isprime(a*a):
        p += 1
    if isprime(a*a - a + 1):
        p += 1
    if isprime(a*a - 2*a + 2):
        p += 1
    if isprime(a*a - 3*a + 3):
        p += 1

print a

t2 = time.clock()
print 'Elapsed time: ', t2-t1

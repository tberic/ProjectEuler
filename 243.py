import time
t1 = time.clock()

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


r = 15499./94744
d = 50000
while (EulerPhi(d) >= r*(d-1)):
    d += 1
    print d, float(EulerPhi(d))/(d-1)

print d

t2 = time.clock()
print 'Elapsed time: ', t2-t1

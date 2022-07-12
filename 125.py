import math
import time
t1 = time.clock()

def palin(x):
    y = x
    while (y > 0):
        x = x*10 + y%10
        y /= 10
    return x

def palin2(x):
    y = x/10
    while (y > 0):
        x = x*10 + y%10
        y /= 10
    return x

def sumsqr(x):
    #N = int(math.pow(3*x, 1./3))
    #for n in range(1, N+1):
    #    a = 1
        


    return False

N = 1100
t = [i*(i+1)*(2*i+1)/6 for i in range(N)]

sum = 0
for x in range(1, 10**4):
    if sumsqr(palin2(x)):
        sum += palin2(x)
    if sumsqr(palin(x)):
        sum += palin(x)

print sum

t2 = time.clock()
print 'Elapsed time: ', t2-t1

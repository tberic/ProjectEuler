import time
t1 = time.clock()

N = 10**1
b = 1
a = 0
E = 0

for i in range(1, N):
    E += float(i*a)/1000**i
    a += b*(i-1)
    b *= 1000**(i-1) - (i-1)
    print b, a, E



t2 = time.clock()
print 'Elapsed time: ', t2-t1

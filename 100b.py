import math
import time
t1 = time.clock()

def blue(x):
	return int( math.sqrt( 2*x**2 - 2*x + 1 ) )

#N = 1000000058045
N = 803762

b = blue(N)
n = N
while n < 10**12:
        while b*b < 2*n**2 - 2*n + 1 or b % 2 == 0:
            n += 1
            #print n
            b = blue(n)
        print n, (1+b)/2
        n = int(5.8*n)
        b = blue(n)

t2 = time.clock()
print 'Elapsed time: ', t2-t1

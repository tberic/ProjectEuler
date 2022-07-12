import math
import time
t1 = time.clock()

M = 100
N = 10000

#cnt = 0
#for x in range(M+1, N+1):
#    for y in range(x, N+1):
#        if int(float(y**2)/x**2) % 2 == 1:
#            cnt += 1
#
#print cnt

s = 0
a = int(float(N)/math.sqrt(2))
for x in range(M+1, N+1):
    for k in range(1, N**2/(2*x**2)+1):
        s += math.floor(math.sqrt(2*k)*x) - math.ceil(math.sqrt(2*k - 1)*x)

print s

t2 = time.clock()
print 'Elapsed time: ', t2-t1

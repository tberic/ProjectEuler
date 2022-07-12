import time
t1 = time.clock()

N = 1000

s = 0
for a in range(3, N+1):
    s += 2*a*((a-1)/2)

print s

t2 = time.clock()
print 'Elapsed time: ', t2-t1

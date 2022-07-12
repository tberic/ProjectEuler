import time
t1 = time.clock()

N = 50

a = [1 for i in range(N+1)]
a[3] = 2

for i in range(4, N+1):
    a[i] = 2*a[i-1] - a[i-2] + a[i-4]

print a[N]

t2 = time.clock()
print 'Elapsed time: ', t2-t1

import time
t1 = time.clock()

N = 50

a = [1 for i in range(N+1)]
b = [1 for i in range(N+1)]
c = [1 for i in range(N+1)]

for i in range(2, N+1):
    a[i] = a[i-1] + a[i-2]
for i in range(3, N+1):
    b[i] = b[i-1] + b[i-3]
for i in range(4, N+1):
    c[i] = c[i-1] + c[i-4]

print a[N] + b[N] + c[N] - 3

t2 = time.clock()
print 'Elapsed time: ', t2-t1

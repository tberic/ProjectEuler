import time
t1 = time.clock()

a = [1 for i in range(51)]
a[2] = 2
a[3] = 4
a[4] = 8

for i in range(5, 51):
    a[i] = a[i-1] + a[i-2] + a[i-3] + a[i-4]

print a[50]

t2 = time.clock()
print 'Elapsed time: ', t2-t1

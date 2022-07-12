import time
t1 = time.clock()

N = 10**6
m = 50

a = [1 for i in range(m+2)]
a[m] = 2

i = m+1
while a[m+1] < N:
    a[m+1] = 2*a[m] - a[m-1] + a[0]
    i += 1
    #print a[m+1]
    for j in range(m+1):
        a[j] = a[j+1]

print i-1

t2 = time.clock()
print 'Elapsed time: ', t2-t1

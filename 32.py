import time
import itertools
t1 = time.clock()

v = [0 for i in range(10**4)]

d = list(itertools.permutations([1,2,3,4,5,6,7,8,9]))

s = 0
for a in d:
    x = a[0]
    y = a[1]*10**3 + a[2]*10**2 + a[3]*10 + a[4]
    z = a[5]*10**3 + a[6]*10**2 + a[7]*10 + a[8]
    if x * y == z and v[z] == 0:
            v[z] = 1
            s += z
    x = a[0]*10 + a[1]
    y = a[2]*10**2 + a[3]*10 + a[4]
    z = a[5]*10**3 + a[6]*10**2 + a[7]*10 + a[8]
    if x * y == z and v[z] == 0:
            v[z] = 1
            s += z

print s

t2 = time.clock()
print 'Elapsed time: ', t2-t1

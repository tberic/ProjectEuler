import math
import time
t1 = time.clock()

#preciznost: 6 decimala
def contfrac(x):
    c = []
    used = []
    k = 0
    while True:
        y = float( str(x)[:5] )
        if x == 0 or y in used:
            break
        used.append(y)
        c.append(int(math.floor(x)))
        x -= math.floor(x)
        x = 1./x
        k += 1
    return k-1

cnt = 0
for i in range(2, 10001):
    a = int(math.sqrt(i))
    if a*a < i:
        #print i
        if contfrac(math.sqrt(i)) % 2 == 1:
            cnt += 1

print cnt

t2 = time.clock()
print 'Elapsed time: ', t2-t1

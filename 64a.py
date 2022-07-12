import math
import time
t1 = time.clock()

def contfracsqrt(x):
    arr = []
    arr_m = []
    arr_d = []
    arr_a = []
    m = 0
    d = 1
    a = math.floor(math.sqrt(x))

    k = 0    
    while [m, d, a] not in arr:
        arr.append([m, d, a])
        m = arr[k][1]*arr[k][2] - arr[k][0]
        d = (x - m**2)/arr[k][1]
        a = math.floor( float(math.sqrt(x) + m)/d )
        k += 1
        
    return k - 1

cnt = 0
for i in range(2, 10001):
    a = int(math.sqrt(i))
    if a*a < i:
        if contfracsqrt(i) % 2 == 1:
            cnt += 1

print cnt

t2 = time.clock()
print 'Elapsed time: ', t2-t1

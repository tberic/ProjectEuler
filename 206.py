import math
import time
t1 = time.clock()

def target(x):
    for i in range(10):
        if (x / 10**(2*i)) % 10 != (10-i) % 10:
            return False
    return True

a = int(math.sqrt(1020304050607080900))
b = int(math.sqrt(1929394959697989990))

while a <= b:
    if target(a*a):
        print a
        break
    a += 1
    
t2 = time.clock()
print 'Elapsed time: ', t2-t1

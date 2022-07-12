import math
import time
t1 = time.clock()

def factors(x):
    f = []
    for p in range(2, int(math.sqrt(x)+1)):
        i = 0
        while x % p == 0:
            x //= p
            i += 1
        if i:
            f.append(p)
    if x > 1:
        f.append(x)
    return f

i = 1
while True:
    if len(factors(i)) != 4:
        i += 1
    elif len(factors(i+1)) != 4:
        i += 2
    elif len(factors(i+2)) != 4:
        i += 3
    elif len(factors(i+3)) != 4:
        i += 4
    else:
        break

print i

t2 = time.clock()
print 'Elapsed time: ', t2-t1

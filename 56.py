import time
t1 = time.clock()

def digitalsum(x):
    s = 0
    while (x > 0):
        s += x%10
        x /= 10
    return s

max = 0
for a in range(1, 100):
    for b in range(1, 100):
        t = digitalsum(a**b)
        if t > max:
            max = t

print max

t2 = time.clock()
print 'Elapsed time: ', t2-t1

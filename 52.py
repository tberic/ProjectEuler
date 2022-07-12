import time
t1 = time.clock()

def ok(x, n):
    d1 = digits(1*x)
    d1.sort()
    for i in range(2, n+1):
        d2 = digits(i*x)
        d2.sort()
        if d1 != d2:
            return False
    return True    

def digits(x):
    d = []
    while (x > 0):
        d.append(x%10)
        x /= 10
    return d

i = 1
while not ok(i, 6):
    i += 1

print i

t2 = time.clock()
print 'Elapsed time: ', t2-t1

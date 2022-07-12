import time
t1 = time.clock()

def rmax(a):
    max = 0
    for i in range(1, a):
        if (2*i*a) % (a*a) > max:
            max = (2*i*a) % (a*a)
    return max

N = 1000

s = 0
for a in range(3, N+1):
    s += rmax(a)

print s

t2 = time.clock()
print 'Elapsed time: ', t2-t1

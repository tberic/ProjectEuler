import time
t1 = time.clock()

def sols(n):
    cnt = 0
    for x in range(n+1, 2*n+1):
        a = float(n*x)/(x-n)
        if a == int(a):
            cnt += 1
    return cnt


n = 58024
a = 0
while a <= 1000:
    n += 1
    a = sols(n)
    print n, a

print n

t2 = time.clock()
print 'Elapsed time: ', t2-t1

import time
t1 = time.clock()

def u(r, k):
    return (900-3*k)*r**(k-1)

def s(r, n):
    s = 0
    for k in range(1, n+1):
        s += u(r, k)
    return s

def equal(x, y, eps):
    #return (x - eps < y and y < x + eps)
    return x == y

l = 1.0
r = 1.01
m = (l + r)/2
N = 5000
target = -600*10**9
epsilon = 10**(-13)

while l < r and s(m, N) != target:
    print repr(s(m, N)), repr(m)
    m = (l + r)/2
    if s(m, N) < target:
        r = m-epsilon
    else:
        l = m+epsilon
        
print repr(m)

t2 = time.clock()
print 'Elapsed time: ', t2-t1

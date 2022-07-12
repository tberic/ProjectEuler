import time
t1 = time.clock()

#equal up to 10th decimal place
def equal(a, b, d):
    return (int(a*10**d) == int(b*10**d))
    

def dig(x, n):
    d = [0 for i in range(10)]
    while x:
        d[x % 10] += 1
        if d[x % 10] == n:
            return True
        x /= 10
    return False

N = 10**7

t = 1
s = 0
n = 0
#while not equal(t, s, 10):
while n < N:
    n = n + 1
    if not dig(n, 3):
        #print s
        t = s
        s += 1./n

print s

t2 = time.clock()
print 'Elapsed time: ', t2-t1

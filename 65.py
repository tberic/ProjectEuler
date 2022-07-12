import time
t1 = time.clock()

def gcd(a, b):
    if (b == 0):
        return a
    return gcd(b, a%b)

N = 100

a = 1
b = 0

for k in range(N, 1, -1):
    b, a = a, b
    if k % 3 == 0:
        a = a + 2*(k/3)*b
    else:
        a = a + b

b, a = a, b
a = a + 2*b

a /= gcd(a,b)
b /= gcd(a,b)

s = 0
while (a > 0):
    s += a%10
    a /= 10

print s

t2 = time.clock()
print 'Elapsed time: ', t2-t1

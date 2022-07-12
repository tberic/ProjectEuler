import time

f = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]

def digitsfact(x):
    s = 0
    n = x
    while (x > 0):
        s += f[x%10]
        x = x / 10
    return s == n

t1 = time.clock()

N = 10**5

i = 10
s = 0
while (i < N):
    i = i + 1
    if digitsfact(i):
        s += i

print s

t2 = time.clock()
print 'Elapsed time: ', t2-t1

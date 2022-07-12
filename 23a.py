import math

def divsum(x):
    s = 1

    if (x >= 1 and x <= 3): return 1
    
    a = int(math.sqrt(x))

    for i in range(2, a):
        if (x % i == 0):
            s = s + i
            s = s + x/i
    if (a*a == x) :
        s = s + a    
    elif (x % a == 0):
        s = s + a
        s = s + x/a
    
    return s

def abundant(x):
    return (x < divsum(x))

a = [0 for i in range(28124)]
b = [0 for i in range(28124)]

na = 0
for i in range(1, 28124):
    if abundant(i):
        a[na] = i
        na = na + 1

for i in range(na):
    for j in range(i, na):
        if ( a[i] + a[j] <= 28123):
            b[ a[i]+a[j] ] = 1

s = 0
for i in range(28124):
    if (b[i] == 0): s = s + i

print s

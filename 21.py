import math

def divsum(x):
    s = 1
    a = int(math.sqrt(x))

    for i in range(2, a):
        if (x % i == 0):
            s = s + i
            s = s + x/i
    if (x % a == 0): s = s + a    
    
    return s

s = 0
for i in range(1, 10000):
    t = divsum(i)
    if (i != t and divsum(t) == i ):
        s = s + i

print s

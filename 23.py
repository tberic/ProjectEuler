import math

def divsum(x):
    s = 1
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

s = 0
for i in range(1, 28124):
    a = 12
    while ( a <= i - 12 ):
        if ( abundant(a) and abundant(i-a) ):
            s = s + i
            print i
            break
        a = a + 1
       
print 28123*28124/2-s

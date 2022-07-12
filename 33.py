import time
t1 = time.clock()

def wrongcancel(a,b,c,d):
    if a == c and b*(10*c+d) == d*(10*a+b):
        return 1
    if a == d and b*(10*c+d) == c*(10*a+b):
        return 1
    if b == c and a*(10*c+d) == d*(10*a+b):
        return 1
    if b == d and a*(10*c+d) == c*(10*a+b):
        return 1
    return 0  
        
x = 1
y = 1
for a in range(1, 10):
    for b in range(1, 10):
        for c in range(1, 10):
            for d in range(1, 10):
                if 10*a+b < 10*c+d and wrongcancel(a,b,c,d):
                    x *= 10*a+b
                    y *= 10*c+d
                    print 10*a+b, '/', 10*c+d

print x, y

t2 = time.clock()
print 'Elapsed time: ', t2-t1

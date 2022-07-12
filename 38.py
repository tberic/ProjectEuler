import time
t1 = time.clock()

def pandigital(x):
    d = [0 for i in range(10)]
    d[0] = 1
    while (x > 0):
        if d[x%10]:
            return 0
        d[x%10] = 1
        x = x / 10
    return sum(d) == 10

for a in range(9, 0, -1):
    for b in range(9, 0, -1):
        for c in range(9, 0, -1):
            x = 9000+100*a+10*b+c
            y = 2*x
            if pandigital(x*100000+y):
                print x*100000+y
                break

        
t2 = time.clock()
print 'Elapsed time: ', t2-t1

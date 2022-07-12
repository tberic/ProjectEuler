import time
t1 = time.clock()

def pandigital(x):
    d = [0 for i in range(9)]
    while x > 0:
        if x%10 != 0:
            d[x%10-1] = 1
        x /= 10
    if 0 in d:
        return False
    return True
        
def target(x):
    s = str(x)
    return pandigital(int(s[-9:])) and pandigital(int(s[:9]))        

a = 1
b = 1
k = 2
while not target(b):
    k += 1
    a, b = b, a+b
    #print b

print k

t2 = time.clock()
print 'Elapsed time: ', t2-t1

import time

def ispalindromic(x, b):
    a = [0 for i in range(20)]
    nd = 0
    while (x > 0):
        a[nd] = x%b
        nd += 1
        x = x/b

    i = 0
    while (a[i] == a[nd-i-1] and i < nd/2):
        i += 1
    return (i == nd/2)
    

t1 = time.clock()

N = 10**6

s = 0
for i in range(1, N, 2):
    if ( ispalindromic(i, 10) and ispalindromic(i, 2) ):
        s += i

print s

t2 = time.clock()
print 'Elapsed time: ', t2-t1

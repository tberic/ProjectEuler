import math
import time
t1 = time.clock()

def isPalin(x):
    s = str(x)
    i = 0
    while i < len(s)/2 and s[i] == s[len(s)-i-1]:
         i += 1
    return s[i] == s[len(s)-i-1]

N = 30000
t = [i*(i+1)*(2*i+1)/6 for i in range(N)]

used = []

sum = 0
for i in range(N):
    for j in range(i-1):
        if t[i]-t[j] <= 10**8 and t[i]-t[j] not in used and isPalin(t[i]-t[j]):
            sum += t[i]-t[j]
            used.append(t[i]-t[j])
            
print sum

t2 = time.clock()
print 'Elapsed time: ', t2-t1

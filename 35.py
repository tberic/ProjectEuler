#ako treba jos ubrzati, mogu se generirati samo brojevi sa znamenkama 1,3,7,9
import time

L = 6
N = 10**L

t1 = time.clock()

#first generate primes
p = [1 for i in range(N)]
for i in range(2, N):
    if (p[i] == 1):
        j = 2
        while (i*j < N):
            p[j*i] = 0
            j += 1
    
cnt = 4
for l in range(1, L):
    for i in range(10**l, 10**(l+1)):
        if p[i]:
            a = i
            t = 1
            for k in range(l):
                a = (a%10)*10**l + (a/10)
                if (p[a] == 0):
                    t = 0
                    break
            if (t == 1):
                print i
                cnt += 1
        
print cnt

t2 = time.clock()
print 'Time elapsed: ', t2-t1


import time
t1 = time.clock()

def isprime(x):
    if x == 1:
        return 0
    if x in [2, 3, 5, 7]:
        return 1
    if x % 2 == 0 or x % 3 == 0 or x % 5 == 0 or x % 7 == 0:
        return 0
    if x % 6 != 1 and x % 6 != 5:
        return 0
    j = 9
    while (j*j <= x):
        if (x % j == 0):
            return 0
        j += 2
    return 1

def truncatable(x):
    s = 1
    n = x
    while isprime(x):
        s = s*10
        x /= 10
    if x:
        return 0
    while isprime(n):
        n %= s
        s /= 10
    return (n == 0)
        

s = 0
#2 digits
for a in [2, 3, 5, 7]:
    for b in [3, 7]:
        if truncatable(10*a+b):
            print 10*a+b
	    s += 10*a+b


#3 digits
for a in [2, 3, 5, 7]:
    for b in [1, 3, 7, 9]:
        for c in [3, 7]:
            if truncatable(100*a+10*b+c):
                print 100*a+10*b+c
		s += 100*a+10*b+c

#4 digits
for a in [2, 3, 5, 7]:
    for b in [1, 3, 7, 9]:
        for c in [1, 3, 7, 9]:
            for d in [3, 7]:
                if truncatable(1000*a+100*b+10*c+d):
                    print 1000*a+100*b+10*c+d
                    s += 1000*a+100*b+10*c+d

#5 digits
for a in [2, 3, 5, 7]:
    for b in [1, 3, 7, 9]:
        for c in [1, 3, 7, 9]:
            for d in [1, 3, 7, 9]:
                for e in [3, 7]:
                    if truncatable(10000*a+1000*b+100*c+10*d+e):
                        print 10000*a+1000*b+100*c+10*d+e
                        s += 10000*a+1000*b+100*c+10*d+e

#6 digits
for a in [2, 3, 5, 7]:
    for b in [1, 3, 7, 9]:
        for c in [1, 3, 7, 9]:
            for d in [1, 3, 7, 9]:
                for e in [1, 3, 7, 9]:
                    for f in [3, 7]:
                        if truncatable(100000*a+10000*b+1000*c+100*d+10*e+f):
                            print 100000*a+10000*b+1000*c+100*d+10*e+f
                            s += 100000*a+10000*b+1000*c+100*d+10*e+f


#only 11 primes are:
#23
#37
#53
#73
#313
#317
#373
#797
#3137
#3797
#739397

print s

t2 = time.clock()
print 'Elapsed time: ', t2-t1

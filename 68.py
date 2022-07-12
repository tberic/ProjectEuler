from itertools import permutations
import time
t1 = time.clock()

def solved(a):
    return a[0]+a[1]+a[2] == a[3]+a[2]+a[4] and \
           a[3]+a[2]+a[4] == a[5]+a[4]+a[6] and \
           a[5]+a[4]+a[6] == a[7]+a[6]+a[8] and \
           a[7]+a[6]+a[8] == a[9]+a[8]+a[1]

def digit(x):
    if x == 'A':
        return 10
    else:
        return int(x)

def digstring(a):
    s = ['' for i in range(5)]
    s[0] = str(a[0])+str(a[1])+str(a[2])
    s[1] = str(a[3])+str(a[2])+str(a[4])
    s[2] = str(a[5])+str(a[4])+str(a[6])
    s[3] = str(a[7])+str(a[6])+str(a[8])
    s[4] = str(a[9])+str(a[8])+str(a[1])

    t = [a[0], a[3], a[5], a[7], a[9]]
    t.sort()
    if a[0] == t[0]:
        return s[0]+s[1]+s[2]+s[3]+s[4]
    if a[3] == t[0]:
        return s[1]+s[2]+s[3]+s[4]+s[0]
    if a[5] == t[0]:
        return s[2]+s[3]+s[4]+s[0]+s[1]
    if a[7] == t[0]:
        return s[3]+s[4]+s[0]+s[1]+s[2]
    if a[9] == t[0]:
        return s[4]+s[0]+s[1]+s[2]+s[3]

                
concat = ''.join
perm = list(map(concat, permutations('123456789A')))

k = [0 for i in range(10)]

max = ''
for p in perm:
    for i in range(10):
        k[i] = digit(p[i])
    if solved(k):
        s = digstring(k)
        if s > max and len(s) == 16:
            max = s
                
print max

t2 = time.clock()
print 'Elapsed time: ', t2-t1

from itertools import permutations
import time
t1 = time.clock()

def P(k, n):
    if k == 3:
        return n*(n+1)/2
    if k == 4:
        return n*n
    if k == 5:
        return n*(3*n-1)/2
    if k == 6:
        return n*(2*n-1)
    if k == 7:
        return n*(5*n-3)/2
    if k == 8:
        return n*(3*n-2)
    return 0

def noteq(l):
    a = [l[i] for i in range(9)]
    a.sort()
    if a[3]==a[4] or a[4]==a[5] or a[5]==a[6] or a[6]==a[7] or a[7]==a[8]:
        return False
    return True

def cyclic(x, y):
    return x % 100 == y / 100

def ispis(l, k):
    for i in range(3, 9):
        print P(k[i], l[i]),
    print

i = [0, 0, 0, 44, 32, 26, 23, 21, 19]
j = [0, 0, 0, 44, 32, 26, 23, 21, 19]
l = [0, 0, 0, 0, 0, 0, 0, 0, 0]
n = [0, 0, 0, 0, 0, 0, 0, 0, 0]

for k in range(3, 9):
    while P(k, j[k]) <= 9999:
        n[k] += 1
        j[k] += 1

concat = ''.join
perm = list(map(concat, permutations('345678')))

k = [0 for x in range(9)]

for p in perm:
    for x in range(3, 9):
        k[x] = int(p[x-3])
    for l[3] in range(i[k[3]], j[k[3]]):
        for l[4] in range(i[k[4]], j[k[4]]):
            if cyclic(P(k[3], l[3]), P(k[4], l[4])):
                for l[5] in range(i[k[5]], j[k[5]]):
                    if cyclic(P(k[4], l[4]), P(k[5], l[5])):
                        for l[6] in range(i[k[6]], j[k[6]]):
                            if cyclic(P(k[5], l[5]), P(k[6], l[6])):
                                for l[7] in range(i[k[7]], j[k[7]]):
                                    if cyclic(P(k[6], l[6]), P(k[7], l[7])):
                                        for l[8] in range(i[k[8]], j[k[8]]):
                                            if cyclic(P(k[7], l[7]), P(k[8], l[8])) and cyclic(P(k[8], l[8]), P(k[3], l[3])):
                                                if noteq(l):
                                                    print P(k[3], l[3]) + P(k[4], l[4]) + \
                                                          P(k[5], l[5]) + P(k[6], l[6]) + \
                                                          P(k[7], l[7]) + P(k[8], l[8])
                                                    ispis(l, k)

t2 = time.clock()
print 'Elapsed time: ', t2-t1

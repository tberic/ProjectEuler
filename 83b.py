from priodict import priorityDictionary

import time
t1 = time.clock()

f = open('83.txt')
a = [[int(x) for x in l.split(',')] for l in f]
n = len(a)

def neighbors(u):
    x = u % n
    y = u / n
    lst = {}
    if (x > 0):
        lst.append((x-1)*n+y)
    if (y > 0):
        lst.append(x*n+y-1)
    if (x < n-1):
        lst.append((x+1)*n+y)
    if (y < n-1):
        lst.append(x*n+y+1)
    return lst    

D = {}
Q = priorityDictionary()
Q[0] = a[0][0]
for v in Q:
    D[v] = Q[v]
    if v == n*n-1:
        break

    for w in neighbors(v):
        vwLength = D[v] + a[w/n][w%n]
        if w in D:
            if vwLength < D[w]:
                print 'error'
        elif w not in Q or vwLength < Q[w]:
            Q[w] = vwLength

print D

f.close()

t2 = time.clock()
print 'Elapsed time: ', t2-t1

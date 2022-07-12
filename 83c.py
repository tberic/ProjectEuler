import time
t1 = time.clock()

def neighbors(u):
    x = u / n
    y = u % n
    lst = []
    if (x > 0):
        lst.append((x-1)*n+y)
    if (y > 0):
        lst.append(x*n+y-1)
    if (x < n-1):
        lst.append((x+1)*n+y)
    if (y < n-1):
        lst.append(x*n+y+1)
    return lst    

f = open('83.txt')
a = [[int(x) for x in l.split(',')] for l in f]
n = len(a)

INF = -1
d = [INF for i in range(n*n)]
d[0] = a[0][0]

q = [0]
while len(q) > 0:
    min = INF
    for i in q:
        if min == INF or (d[i] != INF and d[i] < min):
            min = d[i]
            u = i
    q.remove(u)
    #print u, d
    for v in neighbors(u):
        if d[v] == INF or d[u] + a[v/n][v%n] < d[v]:
            d[v] = d[u] + a[v/n][v%n]
            q.append(v)

print d[n*n-1]

f.close()

t2 = time.clock()
print 'Elapsed time: ', t2-t1

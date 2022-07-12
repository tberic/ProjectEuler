import time
t1 = time.clock()

def neighbors(u):
    x = u % n
    y = u / n
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
dist = [INF for i in range(n*n)]
dist[0] = 0
q = [0]
while len(q):
    min = 0
    u = 0
    for i in range(len(q)):
        if dist[q[i]] != INF and dist[q[i]] < min:
            min = dist[q[i]]
            u = q[i]
    q.remove(u)
    for v in neighbors(u):
        if dist[v] == INF or dist[u] + a[v/n][v%n] < dist[v]:
            dist[v] = dist[u] + a[v/n][v%n]

print dist

f.close()

t2 = time.clock()
print 'Elapsed time: ', t2-t1

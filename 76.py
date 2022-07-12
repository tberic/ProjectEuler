import time
t1 = time.clock()

N = 100
p = [[0 for j in range(N+1)] for i in range(N+1)]

p[1][1] = 1

for n in range(1, N+1):
    p[n][n] = 1
    for k in range(n-1, 0, -1):
        p[n][k] = p[n][k+1] + p[n-k][k]

print p[N][1]-1

t2 = time.clock()
print 'Elapsed time: ', t2-t1

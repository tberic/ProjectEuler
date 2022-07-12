import time
t1 = time.clock()

M = 10**6
N = 10000
p = [[0 for j in range(N+1)] for i in range(N+1)]

p[1][1] = 1

n = 1
while True:
    p[n][n] = 1
    for k in range(n-1, 0, -1):
        p[n][k] = (p[n][k+1] + p[n-k][k]) % M
    if p[n][1] == 0:
        break
    n += 1

print n

t2 = time.clock()
print 'Elapsed time: ', t2-t1

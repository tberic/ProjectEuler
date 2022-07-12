import time
t1 = time.clock()

N = 101
C = [[0 for j in range(N)] for i in range(N)]

for n in range(N):
    C[n][0] = 1
    C[n][n] = 1

cnt = 0
for n in range(N):
    for k in range(1, n+1):
        C[n][k] = C[n-1][k-1] + C[n-1][k]
        if (C[n][k] > 10**6):
            cnt += 1

print cnt

t2 = time.clock()
print 'Elapsed time: ', t2-t1

#popraviti rekurzije, dosta je komplicirano
#jos uvijek je komplicirano
import time
t1 = time.clock()

N = 40
A = [[[0 for k in range(10)] for j in range(10)] for i in range(N+1)]

for l in range(10):
    for k in range(l, 10):
        A[1][k][l] = 1

for n in range(2, N+1):
    for l in range(9):
        A[n][l][l] = A[n-1][l+1][l] + A[n-1][l+1][l+1]
        for k in range(l+1, 9):
            A[n][k][l] = A[n-1][k-1][l] + A[n-1][k+1][l]
        A[n][9][l] = A[n-1][l+1][l] + A[n-1][l+1][l+1]
    A[n][9][9] = 0

s = 0
for n in range(1, N+1):
    for k in range(1, 10):
        s += A[n][k][0]

print s

t2 = time.clock()
print 'Elapsed time: ', t2-t1

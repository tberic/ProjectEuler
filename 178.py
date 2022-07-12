#popraviti rekurzije, dosta je komplicirano
import time
t1 = time.clock()

N = 40
A = [[[0 for k in range(10)] for j in range(10)] for i in range(N+1)]
B = [[[0 for k in range(10)] for j in range(10)] for i in range(N+1)]
T = [[0 for j in range(10)] for i in range(N+1)]

A[9][1] = 1
B[9][8] = 1

T[10][0] = 1
T[10][9] = 1

for n in range(11, N+1):
    T[n][0] = T[n-1][1]
    for k in range(1, 9):
        T[n][k] = T[n-1][k-1] + T[n-1][k+1]
    T[n][9] = T[n-1][8]

s = 0
for n in range(10, N+1):
    s += sum(T[n][1:])

print s

t2 = time.clock()
print 'Elapsed time: ', t2-t1

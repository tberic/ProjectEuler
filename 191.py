import time
t1 = time.clock()

N = 30

#no L's
s = [[1 for j in range(2)] for i in range(N+1)]
s[2][0] = 2
s[2][1] = 2

for n in range(3, N+1):
    s[n][0] = 2*s[n-2][1] + s[n-2][0]
    s[n][1] = s[n-1][1] + s[n-1][0]

#one L
t = [[0 for j in range(2)] for i in range(N+1)]
t[2][0] = 1
t[2][1] = 1

for n in range(3, N+1):
    t[n][0] = s[n-1][0]
    t[n][1] = s[n-1][1]
    for k in range(2, n):
        t[n][0] += (s[k-1][1] + s[k-1][0])*s[n-k][0]
        t[n][1] += (s[k-1][1] + s[k-1][0])*s[n-k][1]

print s[N][0]+s[N][1] + t[N][0]+t[N][1] + s[N-1][0]+s[N-1][1]

t2 = time.clock()
print 'Elapsed time: ', t2-t1

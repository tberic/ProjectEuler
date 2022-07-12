import time
t1 = time.clock()

N = 101
a = [[1 for j in range(N)] for i in range(N)]

cnt = 0
#print 1
for i in range(2, N):
#    print 1,
    for j in range(1, i-1):
        a[i][j] = a[i-1][j-1] + a[i-1][j]
        if a[i][j] % 7 == 0:
            #print a[i][j],
            cnt += 1
            if j % 7 == 0:
                print i, j
        #    print '[',a[i][j], ']',
    #print 1

print cnt

t2 = time.clock()
print 'Elapsed time: ', t2-t1

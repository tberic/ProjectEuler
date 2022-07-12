import time
t1 = time.clock()

A = [0 for i in range(37)] #6 x 6
B = [0 for i in range(37)] #9 x 4

for a in range(1, 7):
    for b in range(1, 7):
        for c in range(1, 7):
            for d in range(1, 7):
                for e in range(1, 7):
                    for f in range(1, 7):
                        A[a+b+c+d+e+f] += 1

for x1 in range(1, 5):
    for x2 in range(1, 5):
        for x3 in range(1, 5):
            for x4 in range(1, 5):
                for x5 in range(1, 5):
                    for x6 in range(1, 5):
                        for x7 in range(1, 5):
                            for x8 in range(1, 5):
                                for x9 in range(1, 5):
                                    B[x1+x2+x3+x4+x5+x6+x7+x8+x9] += 1

cnt = 0
for i in range(37):
    for j in range(i+1, 37):
        cnt += A[i]*B[j]

print cnt

print repr( float(cnt)/(4**9*6**6) )

t2 = time.clock()
print 'Elapsed time: ', t2-t1

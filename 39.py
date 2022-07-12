import time
t1 = time.clock()

N = 1000
max = 0
for p in range(14, N+1):
    cnt = 0
    for a in range(1, p-1):
        for b in range(1, p-a):
            if a**2 + b**2 == (p-a-b)**2:
                cnt += 1
    if cnt > max:
        max = cnt
        maxp = p

print max, maxp

t2 = time.clock()
print 'Elapsed time: ', t2-t1

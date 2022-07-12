import time
t1 = time.clock()

def digits(x):
    d = []
    while (x > 0):
        d.append(x%10)
        x /= 10
    return d

def win(x):
    d = digits(x)
    for i in range(len(d)):
        for j in range(i+1, len(d)):
            if d[i] + d[j] == 10:
                return 1
    return 0

N = 10**2

cnt = 0
for i in range(N):
    cnt += win(i)

print cnt

t2 = time.clock()
print 'Elapsed time: ', t2-t1

import time
t1 = time.clock()

def rightangle(x1, y1, x2, y2):
    if x1 == 0 and y1 == 0 or x2 == 0 and y2 == 0 or x1 == x2 and y1 == y2:
        return False
    a = x1**2 + y1**2
    b = x2**2 + y2**2
    c = (x1-x2)**2 + (y1-y2)**2
    if c >= a and c >= b:
        return a + b == c
    if b >= a and b >= c:
        return a + c == b
    if a >= b and a >= c:
        return b + c == a

N = 50

cnt = 0
for x1 in range(N+1):
    for x2 in range(N+1):
        for y1 in range(N+1):
            for y2 in range(N+1):
                if rightangle(x1, y1, x2, y2):
                    cnt += 1

print cnt/2

t2 = time.clock()
print 'Elapsed time: ', t2-t1

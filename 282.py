#not good
import time
t1 = time.clock()

def A(m, n):
    if m == 0:
        return n+1
    if n == 0:
        return A(m-1, 1)
    return A(m-1, A(m, n-1))

s = A(0, 0) + A(1, 1) + A(2, 2) + A(3, 3)

#A(4, 4)
t = 1
for i in range(7+1):
    t = 2**t
print t


s += t


#A(5, 5)



t2 = time.clock()
print 'Elapsed time: ', t2-t1

#not good
import time
t1 = time.clock()

a = [[0 for j in range(4)] for i in range(4)]

def positive():
    for i in range(4):
        for j in range(4):
            if a[i][j] < 0:
                return False
    return True

cnt = 0
for i11 in range(10):
    a[0][0] = i11
    for i12 in range(10):
        a[0][1] = i12
        for i13 in range(10):
            a[0][2] = i13
            for i14 in range(10):
                a[0][3] = i14
                s = a[0][0] + a[0][1] + a[0][2] + a[0][3]
                for i21 in range(10):
                    a[1][0] = i21
                    for i22 in range(10):
                        a[1][1] = i22
                        for i23 in range(10):
                            a[1][2] = i23
                            a[1][3] = s - (a[1][0] + a[1][1] + a[1][2])
                            for i31 in range(10):
                                a[2][0] = i31
                                for i33 in range(10):
                                    a[2][2] = i33
                                    a[3][2] = s - (a[0][2] + a[1][2] + a[2][2])
                                    a[3][3] = s - (a[0][0] + a[1][1] + a[2][2])
                                    a[2][3] = s - (a[0][3] + a[1][3] + a[3][3])
                                    a[3][0] = s - (a[0][0] + a[1][0] + a[2][0])
                                    a[3][1] = s - (a[3][0] + a[3][2] + a[3][3])
                                    a[2][1] = s - (a[2][0] + a[2][2] + a[2][3])
                                    if positive():
                                        cnt += 1

print cnt

t2 = time.clock()
print 'Elapsed time: ', t2-t1

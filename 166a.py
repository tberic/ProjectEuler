#ispalo je 14957103, a to nije tocno
#1750 sec
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
for x1 in range(10):
    a[0][0] = x1
    for x2 in range(10):
        a[0][1] = x2
        for x3 in range(10):
            a[0][2] = x3
            for x4 in range(10):
                a[0][3] = x4
                s = a[0][0] + a[0][1] + a[0][2] + a[0][3]
                for x5 in range(10):
                    a[1][0] = x5
                    for x6 in range(10):
                        a[2][0] = x6
                        a[3][0] = s - (a[0][0] + a[1][0] + a[2][0])
                        if a[3][0] < 0:
                            break
                        for x7 in range(10):
                            a[1][1] = x7
                            for x8 in range(10):
                                a[2][2] = x8
                                a[3][3] = s - (a[0][0] + a[1][1] + a[2][2])
                                if a[3][3] < 0:
                                    break
                                for x9 in range(10):
                                    a[2][3] = x9
                                    a[1][3] = s - (a[0][3] + a[2][3] + a[3][3])
                                    if a[1][3] < 0:
                                        continue
                                    a[1][2] = s - (a[1][0] + a[1][1] + a[1][3])
                                    if a[1][2] < 0:
                                        continue
                                    a[3][2] = s - (a[0][2] + a[1][2] + a[2][2])
                                    if a[3][2] < 0:
                                        continue
                                    a[2][1] = s - (a[3][0] + a[1][2] + a[0][3])
                                    if a[2][1] < 0 or a[2][0] + a[2][1] + a[2][2] + a[2][3] != s:
                                        continue
                                    a[3][1] = s - (a[0][1] + a[1][1] + a[2][1])
                                    if a[3][1] < 0 or a[3][0] + a[3][1] + a[3][2] + a[3][3] != s:
                                        continue
                                    cnt += 1

print cnt

t2 = time.clock()
print 'Elapsed time: ', t2-t1

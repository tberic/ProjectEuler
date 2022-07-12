import time
t1 = time.clock()

def ispis():
    print x1, x2, x3, x4
    print x5, x6, x7, y1
    print z1, z2, x8, y4
    print z3, z4, y3, y2
    print

cnt = 0
for x1 in range(10):
    for x2 in range(10):
        for x3 in range(10):
            for x4 in range(10):
                s = x1 + x2 + x3 + x4
                for x5 in range(s + 1):
                    for x6 in range(s-x5 + 1):
                        for x7 in range(s-x5-x6 + 1):
                            y1 = s - x5 - x6 - x7
                            for x8 in range( min(s-x3-x7, s-x1-x6) + 1 ):
                                y2 = s - x1 - x6 - x8
                                y3 = s - x3 - x7 - x8
                                y4 = s - x4 - y1 - y2
                                if y4 < 0:
                                    break
                                if (s - x1 - x5 - x8 - y4 + x4 + x7) % 2 == 1:
                                    break
                                z1 = (s - x1 - x5 - x8 - y4 + x4 + x7) / 2
                                if z1 < 0:
                                    break
                                z2 = s - x8 - y4 - z1
                                if z2 < 0:
                                    break
                                z3 = s - x1 - x5 - z1
                                if z3 < 0:
                                    break
                                z4 = x8 + y4 - x2 - x6 + z1
                                if z4 < 0:
                                    break
                                cnt += 1
                                #ispis()

print cnt

t2 = time.clock()
print 'Elapsed time: ', t2-t1

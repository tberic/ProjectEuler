import math

def area(x1, y1, x2, y2, x3, y3):
    return abs(x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2))/2.

def inside(x1, y1, x2, y2, x3, y3, x0, y0):
    if  area(x1, y1, x2, y2, 0, 0) + area(x1, y1, 0, 0, x3, y3) + area(0, 0, x2, y2, x3, y3) == area(x1, y1, x2, y2, x3, y3):
            return True
    return False

f = open('102.txt')

cnt = 0
for l in f:
    p = [int(x) for x in l.split(',')]
    if inside(p[0], p[1], p[2], p[3], p[4], p[5], 0, 0):
        cnt += 1

print cnt

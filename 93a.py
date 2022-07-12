from itertools import permutations
import time
t1 = time.clock()

def op(a, c, b):
    if c == '+':
        return a+b
    if c == '-':
        return a-b
    if c == '*':
        return a*b
    if c == '/':
        if b == 0:
            return -1000
        else:
            return float(a)/b

def op3(a, c1, b, c2, c):
    if c1 in ['*', '/']:
        return op(op(a, c1, b), c2, c)
    elif c1 == '+':
        return op(a, c1, op(b, c2, c))
    else:
        if c2 in ['*', '/']:
            return op(a, c1, op(b, c2, c))
        else:
            return op(op(a, c1, b), c2, c)

def op4(a, c1, b, c2, c, c3, d):
    if c1 in ['*', '/']:
        return op3(op(a, c1, b), c2, c, c3, d)
    elif c1 == '+':
        return op(a, c1, op3(b, c2, c, c3, d))
    else:
        if c2 in ['*', '/'] and c3 in ['*', '/']:
            return op(a, c1, op3(b, c2, c, c3, d))
        elif c2 in ['*', '/'] and c3 not in ['*', '/']:
            return op3(a, c1, op(b, c2, c), c3, d)
        elif c2 not in ['*', '/'] and c3 in ['*', '/']:
            return op3(a, c1, b, c2, op(c, c3, d))
        else:
            return op3(op(a, c1, b), c2, c, c3, d)

def combinations(i, j, k, l):
    num = []
    concat = ''.join
    perm = list(map(concat, permutations(str(i)+str(j)+str(k)+str(l))))
    for pp in perm:
        a = int(pp[0])
        b = int(pp[1])
        c = int(pp[2])
        d = int(pp[3])
        for c1 in ['+', '-', '*', '/']:
            for c2 in ['+', '-', '*', '/']:
                for c3 in ['+', '-', '*', '/']:
                    p[0] = op4(a, c1, b, c2, c, c3, d)
                    p[1] = op3(op(a, c1, b), c2, c, c3, d)
                    p[2] = op(op3(a, c1, b, c2, c), c3, d)
                    p[3] = op3(a, c1, op(b, c2, c), c3, d)
                    p[4] = op(a, c1, op3(b, c2, c, c3, d))
                    p[5] = op3(a, c1, b, c2, op(c, c3, d))
                    p[6] = op(op(a, c1, b), c2, op(c, c3, d))
                    p[7] = op(op(a, c1, op(b, c2, c)), c3, d)
                    p[8] = op(op(op(a, c1, b), c2, c), c3, d)
                    p[9] = op(a, c1, op(op(b, c2, c), c3, d))
                    p[10] = op(a, c1, op(b, c2, op(c, c3, d)))
                    for i in range(11):
                        if p[i] > 0 and p[i] == int(p[i]) and p[i] not in num:
                            num.append(p[i])
    num.sort()
    return num
    

p = [0 for i in range(11)]
max = 0
for a in range(10):
    for b in range(a+1, 10):
        for c in range(b+1, 10):
            for d in range(c+1, 10):
                num = combinations(a, b, c, d)
                i = 0
                while i < len(num) and num[i] == i+1:
                    i += 1
                if i > max:
                    max = i
                    maxi = (a, b, c, d)

print max, maxi                            

t2 = time.clock()
print 'Elapsed time: ', t2-t1

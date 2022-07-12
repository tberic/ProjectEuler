import time
t1 = time.clock()

def paranthesize(s):
    a = '(((('
    for i in range(len(s)):
        if s[i] == '(':
            a += '(((('
        if s[i] == ')':
            a += '))))'
        if s[i] == '*':
            a += '))*(('
        if s[i] == '/':
            a += '))/(('
        if s[i] == '*':
            a += '))*(('
        if s[i] == '+':
            a += ')))+((('
        if s[i] == '-':
            a += ')))-((('
        if s[i] in "0123456789":
            a += s[i]
            
    return a+'))))'

def parse(s, a, b):
    p = 0
    while a <= b:
        if s[a] == '(':
            t = 0
            i = a+1
            while s[i] != ')' or t > 0:
                if s[i] == '(':
                    t += 1
                if s[i] == ')':
                    t -= 1
                i += 1
            return parse(s, a+1, i-1)
            a = i+1
            continue
        if s[a] == '*':
            return p * parse(s, a+1, b)
        if s[a] == '/':
            return float(p) / parse(s, a+1, b)
        if s[a] == '+':
            return p + parse(s, a+1, b)
        if s[a] == '-':
            return p - parse(s, a+1, b)
        if s[a] in "0123456789":
            p = int(s[a])
            a += 1
    return p

       
s = ["" for i in range(11)]
max = 0
for a in range(10):
    for b in range(a+1, 10):
        for c in range(b+1, 10):
            for d in range(c+1, 10):
                num = []
                for c1 in ['+', '-', '*', '/']:
                    for c2 in ['+', '-', '*', '/']:
                        for c3 in ['+', '-', '*', '/']:
                            s[0] = str(a)+c1+str(b)+c2+str(c)+c3+str(d)
                            s[1] = '('+str(a)+c1+str(b)+')'+c2+str(c)+c3+str(d)
                            s[2] = '('+str(a)+c1+str(b)+c2+str(c)+')'+c3+str(d)
                            s[3] = str(a)+c1+'('+str(b)+c2+str(c)+')'+c3+str(d)
                            s[4] = str(a)+c1+'('+str(b)+c2+str(c)+c3+str(d)+')'
                            s[5] = str(a)+c1+str(b)+c2+'('+str(c)+c3+str(d)+')'
                            s[6] = '('+str(a)+c1+str(b)+')'+c2+'('+str(c)+c3+str(d)+')'
                            s[7] = '('+str(a)+c1+'('+str(b)+c2+str(c)+'))'+c3+str(d)
                            s[8] = '(('+str(a)+c1+str(b)+')'+c2+str(c)+')'+c3+str(d)
                            s[9] = str(a)+c1+'(('+str(b)+c2+str(c)+')'+c3+str(d)+')'
                            s[10] = str(a)+c1+'('+str(b)+c2+'('+str(c)+c3+str(d)+'))'
                            for k in range(11):
                                s[k] = paranthesize(s[k])
                                res = parse(s[k], 0, len(s[k])-1)
                                if res > 0 and res == int(res) and res not in num:
                                    num.append(res)
                num.sort()
                i = 0
                while i < len(num) and num[i] == i+1:
                    i += 1
                if i > max:
                    max = i
                    maxi = (a, b, c, d)

print max, maxi                            

t2 = time.clock()
print 'Elapsed time: ', t2-t1

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
            p = parse(s, a+1, i-1)
            a = i+1
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

       
t2 = time.clock()
print 'Elapsed time: ', t2-t1

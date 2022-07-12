def sumdigits(x, e):
    s = 0
    while (x > 0):
        s = s + (x%10)**e
        x = x/10
    return s

s = 0
for i in range(10, 999999):
    if i == sumdigits(i, 5):
        s = s + i

print s

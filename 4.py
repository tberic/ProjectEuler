def reverse(x):
    s = 0
    while (x > 0):
        s = s*10 + x%10
        x = x/10
    return s

def palindrom(a):
    return (a == reverse(a))

max = 0
for x in range(100, 1000):
    for y in range(x, 1000):
        if palindrom(x*y) and x*y > max:
            max = x*y
            a = x
            b = y

print a, b, a*b

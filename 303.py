def only12(x):
    while (x > 0):
        if (x % 10 > 2):
            return 0
        x = x / 10

    return 1

def f(n):
    t = n
    while (not only12(t)):
        t += n
    return t

s = 0
for n in range(1, 10001):
    s += f(n)/n
    print n

print s

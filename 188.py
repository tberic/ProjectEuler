def powermod(a, b, n):
    x = a
    y = 1
    while (b > 0):
        if (b % 2 == 1):
            y = y*x % n
        x = x*x % n
        b = b / 2
    return y

a = 1777
b = 1855
N = 10**8

t = 1
for i in range(1, b+1):
    t = powermod(a, t, N)

print t

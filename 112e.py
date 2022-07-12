def increasing(x):
    t = x%10
    x = x/10

    while (x > 0):
        if (x%10 - t > 0):
            return 0
        t = x % 10
        x = x / 10
    return 1

def decreasing(x):
    t = x%10
    x = x/10

    while (x > 0):
        if (x%10 - t < 0):
            return 0
        t = x % 10
        x = x / 10
    return 1

def bouncy(x):
        return (not increasing(x) and not decreasing(x))

cnt = 0
i = 1
while (1):
    if bouncy(i): cnt = cnt + 1
    if (cnt == 99*i/100 and (99*i) % 100 == 0):
                print i
                break

    i = i + 1

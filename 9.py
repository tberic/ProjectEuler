for a in range(1, 999):
    for b in range(1, 999):
        if (a*a + b*b == (1000-a-b)*(1000-a-b)):
            print a, b

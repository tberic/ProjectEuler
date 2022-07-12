import time
t1 = time.clock()

M = 10**6
N = 10**5
aiPn = [0 for i in range(N)]
aiPn[1] = 1

def CalcPn(n):
    if n < 0:
        return 0

    if aiPn[n] > 0:
        return aiPn[n]

    Pn = 0
    for k in range(1, n+1):
        n1 = n - k*(3*k - 1)/2
        n2 = n - k*(3*k + 1)/2

        Pn1 = CalcPn(n1)
        Pn2 = CalcPn(n2)

        if k%2 == 1:
            Pn += Pn1 + Pn2
        else:
            Pn -= Pn1 + Pn2

    aiPn[n] = Pn
    return Pn


#checked up to 31500
n = 3
while n < N:
    t = CalcPn(n)
    if t % M == 0:
        break
    print n
    n += 1

print n+1

t2 = time.clock()
print 'Elapsed time: ', t2-t1

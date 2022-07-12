import time
t1 = time.clock()

def palindrome(x):
    s = str(x)
    n = len(s)
    i = 0
    while s[i] == s[n-i-1] and i < n/2:
        i += 1
    return i == n/2

def reverse(x):
    s = 0
    while (x > 0):
        s = s*10 + (x%10)
        x /= 10
    return s

def Lychrel(x):
    n = 0
    x += reverse(x)
    while not palindrome(x) and n < 50:
        x += reverse(x)
        n += 1
    return (n == 50)

N = 10000
cnt = 0
for i in range(N):
    if Lychrel(i):
        cnt += 1       

print cnt

t2 = time.clock()
print 'Elapsed time: ', t2-t1

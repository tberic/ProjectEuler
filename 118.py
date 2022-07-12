#ispada 61138
#no, cini mi se da vise puta broji ista rjesenja
from itertools import permutations
import time
t1 = time.clock()

fact = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]

def isprime(x):
    if x == 1:
        return 0
    if x in [2, 3, 5, 7]:
        return 1
    if x % 2 == 0 or x % 3 == 0 or x % 5 == 0 or x % 7 == 0:
        return 0
    if x % 6 != 1 and x % 6 != 5:
        return 0
    j = 9
    while (j*j <= x):
        if (x % j == 0):
            return 0
        j += 2
    return 1

def check(s, t):
    space = 1
    for i in range(len(t)):
        if t[i] == '1':
            s = s[:i+space] + ' ' + s[i+space:]
            space += 1
    nums = s.split(' ')
    a = sorted(nums)
    if a != nums:
        return False
    for x in a:
        if not isprime(int(x)):
            return False
    return True

concat = ''.join
a = list(map(concat, permutations('123456789')))

cnt = 0
for i in range(1, 2**8): #there are no pandigital primes of length 9
    s = bin(i)[2:]
    s = '0'*(8 - len(s)) + s
    t = 0
    for x in a:
        if check(x, s):
            cnt += 1

print cnt



t2 = time.clock()
print 'Elapsed time: ', t2-t1

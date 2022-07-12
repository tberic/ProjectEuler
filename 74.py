import time
t1 = time.clock()

f = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]

def facdig(x):
    s = 0
    while x > 0:
        s += f[x%10]
        x /= 10
    return s
    
def chain(x):
    nums = []
    while x not in nums:
        nums.append(x)
        x = facdig(x)
    return len(nums)

N = 10**6

cnt = 0
for i in range(1, N):
    if chain(i) == 60:
        cnt += 1

print cnt

t2 = time.clock()
print 'Elapsed time: ', t2-t1

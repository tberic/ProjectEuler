import time
t1 = time.clock()

def u(n):
	return (1-n)*(1 + n**2 + n**4 + n**6 + n**8) + n**10

for n in range(1, 10):
	print u(n)


t2 = time.clock()
print 'Elapsed time: ', t2-t1

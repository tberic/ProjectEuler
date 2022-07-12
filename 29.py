import time
t1 = time.clock()

numbers = []

for a in range(2, 101):
	for b in range(2, 101):
		if a**b not in numbers:
			numbers.append(a**b)

print len(numbers)

t2 = time.clock()
print 'Elapsed time: ', t2-t1

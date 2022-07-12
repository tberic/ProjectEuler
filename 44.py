import math
import time
t1 = time.clock()

def P(n):
	return n*(3*n-1)/2

def isP(k):
	a = float(1 + math.sqrt(1 + 24*k))/6
	return a == int(a)

m = 1000
n = 10000
min = 10**10
for i in range(m, n+1):
	for j in range(i+1, n+1):
		if isP(P(i) + P(j)) and isP(P(j) - P(i)):print i, j
			#if P(j) - P(i) < min:
			#	min = P(j) - P(i)
			#	mini = i
			#	minj = j
	
#print min, mini, minj
#print P(mini), P(minj)

t2 = time.clock()
print 'Elapsed time: ', t2-t1

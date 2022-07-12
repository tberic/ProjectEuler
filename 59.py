import time
t1 = time.clock()

f = open('59.txt')

for l in f:
	a = [int(x) for x in l.split(',')]
a1 = [a[i*3] for i in range(len(a)/3+1)]
a2 = [a[i*3+1] for i in range(len(a)/3)]
a3 = [a[i*3+2] for i in range((len(a)-1)/3)]

#for x in range(97, 123):
#	b2 = [a3[i] for i in range(len(a3))]
#	cnt = 0
#	for i in range(len(b2)):
#		b2[i] ^= x
#		if b2[i] >= 65 and b2[i] <= 90 or b2[i] == 32:
#			cnt += 1
#	if float(cnt)/len(b2) > 0.2:
#		print x

#password is: god (103,111,100)

#decrypt
	
s = 0
for i in range(len(a)):
	if i%3 == 0:
		a[i] ^= 103
	if i%3 == 1:
		a[i] ^= 111
	if i%3 == 2:
		a[i] ^= 100
	s += a[i]

for i in range(len(a)):
	print chr(a[i]), 

print
print s

t2 = time.clock()
print 'Elapsed time: ', t2-t1
f.close()

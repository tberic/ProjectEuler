m = 28433
n = 7830457

p = 1
x = 2
while (n > 0):
#	p = (p*2) % 10000000000
#	n = n - 1
	if (n % 2 == 1):
		p = p*x % 10000000000
	x = x*x % 10000000000
	n = n / 2

p = p*m % 10000000000
print p + 1

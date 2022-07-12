def increasing(x):
	t = x%10
	x = x/10

	while (x > 0):
		if (x%10 - t > 0):
			return 0
		t = x % 10
		x = x / 10
	return 1

def decreasing(x):
	t = x%10
	x = x/10

	while (x > 0):
		if (x%10 - t < 0):
			return 0
		t = x % 10
		x = x / 10
	return 1

#maybe has a problem, try and fix it
def bouncy(x):
	if (x < 100):
		return 0
	t = x%10
	x = x/10
	smjer = x%10 - t

	while (x > 0):
		if ((x%10 - t)*smjer < 0):
			return 1
		t = x % 10
		x = x / 10
	return 0

cnt = 9*2178
i = 21780
while (1):
	if bouncy(i): cnt = cnt + 1
	if (float(cnt)/i >= 0.99): break
	i = i + 1

	if (i % 100000 == 0): print cnt, i, float(cnt)/i

print i

#sb = 0
#si = 0
#sd = 0
#for i in range(1000000):
#        if increasing(i):
#                si = si + 1
#        elif decreasing(i):
#                sd = sd + 1
#        else:
#                sb = sb + 1
#
#print si, sd, sb

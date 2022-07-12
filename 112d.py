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

A = [[0 for k in range(11)] for n in range(101)] #increasing
B = [[0 for k in range(11)] for n in range(101)] #decreasing
S = [[0 for k in range(11)] for n in range(101)] #bouncy

for k in range(10):
	A[1][k] = 1
	B[1][k] = 1

A[1][10] = 10
B[1][10] = 10

for k in range(10):
	A[2][k] = 10-k
	B[2][k] = k+1

B[2][0] = 10

A[2][10] = 55
B[2][10] = 64

for n in range(3, 101):
	for k in range(10):
		for l in range(k, 10):
			A[n][k] = A[n][k] + A[n-1][l]
		for l in range(1, k+1):
			B[n][k] = B[n][k] + B[n-1][l]
		B[n][k] = B[n][k] + 1
		B[n][0] = B[n-1][10]

		S[n][k] = 10**(n-1) + 1 - A[n][k] - B[n][k]
		S[n][0] = 10**(n-1) + 9*(n-1) + 1 - A[n-1][10] - B[n-1][10]
	
	for k in range(10):	
		A[n][10] = A[n][10] + A[n][k]
		B[n][10] = B[n][10] + B[n][k]
	S[n][10] = 10**n + 9*n + 1 - A[n][10] - B[n][10]

#search for 90% bouncy ratio
s = S[6][10]
i = 10**6
while(1):
        if bouncy(i):
                s += 1
        if (float(s)/i >= 0.99):
                break
        i += 1

        if (i % 100000 == 0):
                print s, i, float(s)/i

print i

#print 10**100-1 - S[100][10]

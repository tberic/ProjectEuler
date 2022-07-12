A = [[0 for k in range(11)] for n in range(101)] #increasing
B = [[0 for k in range(11)] for n in range(101)] #decreasing
#S = [[0 for k in range(11)] for n in range(101)] #bouncy

for k in range(10):
	A[2][k] = 10-k
	B[2][k] = k+1
#	S[2][k] = 0

B[2][0] = 10

A[2][10] = 55
B[2][10] = 64
#S[2][10] = 0

print A[2], '\n', B[2], '\n\n'

for n in range(3, 11):
	for k in range(10):
		for l in range(k, 10):
			A[n][k] = A[n][k] + A[n-1][l]
		for l in range(1, k+1):
			B[n][k] = B[n][k] + B[n-1][l]
		B[n][k] = B[n][k] + 1
		B[n][0] = B[n-1][10]
	
		#S[n][k] = S[n-1][10]
		#for l in range(k):
		#	S[n][k] = S[n][k] + A[n-1][l]
		#for l in range(k+1, 10):
		#	S[n][k] = S[n][k] + B[n-1][l]

	for k in range(10):	
		A[n][10] = A[n][10] + A[n][k]
		B[n][10] = B[n][10] + B[n][k]
		#S[n][10] = S[n][10] + S[n][k]

	print A[n], '\n', B[n], '\n\n'

for n in range(2, 11):
        print 10**n + 9*n + 1 - A[n][10] - B[n][10],

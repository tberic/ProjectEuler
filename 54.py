import time
t1 = time.clock()

def v(x):
	if x[0] == 'T':
		return 10
	if x[0] == 'J':
		return 11
	if x[0] == 'Q':
		return 12
	if x[0] == 'K':
		return 13
	if x[0] == 'A':
		return 14
	return int(x[0])
	
def s(x):
	return x[1]

def pack(a):
	return a[0][0]*10**8 + a[1][0]*10**6 + a[2][0]*10**4 + a[3][0]*10**2 + a[4][0]*10**0

def hand(p):
	p.sort()
	p.reverse()
	if p[0][1] == p[1][1] and p[1][1] == p[2][1] and p[2][1] == p[3][1] and p[3][1] == p[4][1]:
#straight flush
		if p[0][0] == p[1][0]+1 and p[1][0] == p[2][0]+1 and p[2][0] == p[3][0]+1 and p[3][0] == p[4][0]+1:
			return 8*10**10 + pack(p)
#flush
		else:
			return 5*10**10 + pack(p)
#4 of a kind
	if p[0][0] == p[1][0] and p[1][0] == p[2][0] and p[2][0] == p[3][0]:
		return 7*10**10 + pack(p)
	if p[1][0] == p[2][0] and p[2][0] == p[3][0] and p[3][0] == p[4][0]:
		p[0], p[4] = p[4], p[0]
		return 7*10**10 + pack(p)
#full house
	if p[0][0] == p[1][0] and p[1][0] == p[2][0] and p[3][0] == p[4][0]:
		return 6*10**10 + pack(p)
	if p[0][0] == p[1][0] and p[2][0] == p[3][0] and p[3][0] == p[4][0]:
		p[1], p[4] = p[4], p[1]
		p[0], p[3] = p[3], p[0]
		return 6*10**10 + pack(p)
#straight
	if p[0][0] == p[1][0]+1 and p[1][0] == p[2][0]+1 and p[2][0] == p[3][0]+1 and p[3][0] == p[4][0]+1:
		return 4*10**10 + pack(p)
#3 of a kind
	if p[0][0] == p[1][0] and p[1][0] == p[2][0]:
		return 3*10**10 + pack(p)
	if p[1][0] == p[2][0] and p[2][0] == p[3][0]:
		p[0], p[3] = p[3], p[0]
		return 3*10**10 + pack(p)
	if p[2][0] == p[3][0] and p[3][0] == p[4][0]:
		p[1], p[4] = p[4], p[1]
		p[0], p[3] = p[3], p[0]
		return 3*10**10 + pack(p)
#2 pairs
	if p[0][0] == p[1][0] and p[2][0] == p[3][0]:
		return 2*10**10 + pack(p)
	if p[0][0] == p[1][0] and p[3][0] == p[4][0]:
		p[2], p[4] = p[4], p[2]
		return 2*10**10 + pack(p)
	if p[1][0] == p[2][0] and p[3][0] == p[4][0]:
		p[2], p[0] = p[0], p[2]
		p[2], p[4] = p[4], p[2]
		return 2*10**10 + pack(p)
#1 pair
	if p[0][0] == p[1][0]:
		return 1*10**10 + pack(p)
	if p[1][0] == p[2][0]:
		p[2], p[0] = p[0], p[2]
		return 1*10**10 + pack(p)
	if p[2][0] == p[3][0]:
		p[2], p[0] = p[0], p[2]
		p[3], p[1] = p[1], p[3]
		return 1*10**10 + pack(p)
	if p[3][0] == p[4][0]:
		p[4], p[0] = p[0], p[4]
		p[3], p[1] = p[1], p[3]
		p[4], p[2] = p[2], p[4]
		return 1*10**10 + pack(p)
#high card
	return pack(p)


p1 = [[0 for j in range(2)] for i in range(5)]
p2 = [[0 for j in range(2)] for i in range(5)]

f = open('54.txt')
player1 = 0
for l in f:
	cards = [[v(x), s(x)] for x in l.split(' ')]
	#suite = [s(x) for x in l.split(' ')]
	p1 = cards[0:5]
	p2 = cards[5:10]

	player1 += hand(p1) > hand(p2)

print player1


t2 = time.clock()
print 'Elapsed time: ', t2-t1

f.close()

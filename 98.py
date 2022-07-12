import math
import time
t1 = time.clock()

def isAnagram(s, t):
    a = sorted(s)
    b = sorted(t)
    return a == b

def word(s, x):
    a = str(x)
    if len(a) != len(s):
        return False

    d = ['1' for i in range(10)]
    for i in range(len(s)):
        if d[int(a[i])] == '1':
            d[int(a[i])] = s[i]
        elif d[int(a[i])] != s[i]:
            return False
    return True

def replaced(s, t, x):
    a = str(x)
    b = [a[i] for i in range(len(a))]
    for i in range(len(b)):
        for j in range(len(s)):
            if t[i] == s[j]:
                b[i] = a[j]
                break
    st = ''.join(b)
    if st[0] == '0':
        return 2
    else:
        return int(st)

def square(x):
    a = int(math.sqrt(x))
    return a*a == x

def isSquare(s, t):
    a = int(math.sqrt(10**(len(s)-1)))
    b = int(math.sqrt(10**len(s)))
    for i in range(b, a-1, -1):
        if word(s, i*i):
            j = replaced(s, t, i*i)
            if square(j):
                if i*i > j:
                    return i*i
                else:
                    return j
    return 0
    
#f = open('98.txt')
#for l in f:
#    a = [x for x in l.split('","')]
#a[0] = a[0][1:]
#a[len(a)-1] = a[len(a)-1][:-1]

N = 10**9
n = int(math.sqrt(N))

anagrams = [["ACT", "CAT"], ["ARISE", "RAISE"], ["BOARD", "BROAD"], ["CARE", "RACE"],
            ["CENTRE", "RECENT"], ["COURSE", "SOURCE"], ["CREATION", "REACTION"],
            ["CREDIT", "DIRECT"], ["DANGER", "GARDEN"], ["DEAL", "LEAD"], ["DOG", "GOD"],
            ["EARN", "NEAR"], ["EARTH", "HEART"], ["EAST", "SEAT"], ["EAT", "TEA"],
            ["EXCEPT", "EXPECT"], ["FILE", "LIFE"], ["FORM", "FROM"], ["FORMER", "REFORM"],
            ["HATE", "HEAT"], ["HOW", "WHO"], ["IGNORE", "REGION"],
            ["INTRODUCE", "REDUCTION"], ["ITEM", "TIME"], ["ITS", "SIT"],
            ["LEAST", "STEAL"], ["MALE", "MEAL"], ["MEAN", "NAME"], ["NIGHT", "THING"],
            ["NO", "ON"], ["NOTE", "TONE"], ["NOW", "OWN"], ["PHASE", "SHAPE"],
            ["POST", "SPOT"], ["POST", "STOP"], ["QUIET", "QUITE"], ["RATE", "TEAR"],
            ["SHEET", "THESE"], ["SHOUT", "SOUTH"], ["SHUT", "THUS"], ["SIGN", "SING"],
            ["SPOT", "STOP"], ["SURE", "USER"], ["THROW", "WORTH"]]

#for i in range(len(a)):
#    for j in range(i+1, len(a)):
#        if isAnagram(a[i], a[j]):

max = 0
for i in range(len(anagrams)):
    a = isSquare(anagrams[i][0], anagrams[i][1])
    if a > max:
        max = a
        maxi = i
        
print max, anagrams[maxi]

t2 = time.clock()
print 'Elapsed time: ', t2-t1

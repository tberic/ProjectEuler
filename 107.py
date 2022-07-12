from collections import defaultdict
from heapq import *

def prim( nodes, edges ):
    conn = defaultdict( list )
    for n1,n2,c in edges:
        conn[ n1 ].append( (c, n1, n2) )
        conn[ n2 ].append( (c, n2, n1) )

    mst = []
    used = set( nodes[ 0 ] )
    usable_edges = conn[ nodes[0] ][:]
    heapify( usable_edges )

    while usable_edges:
        cost, n1, n2 = heappop( usable_edges )
        if n2 not in used:
            used.add( n2 )
            mst.append( ( n1, n2, cost ) )

            for e in conn[ n2 ]:
                if e[ 2 ] not in used:
                    heappush( usable_edges, e )
    return mst

#test
f = open('107.txt')
e = [[str(x) for x in l.split(',')] for l in f]
n = len(e)

nodes = [str(i) for i in range(n)]
edges = []
s1 = 0
for i in range(n):
    for j in range(n):
        if e[i][j][0] != '-':
            edges.append((str(i), str(j), int(e[i][j])))
            s1 += int(e[i][j])
   
#nodes = list("ABCDEFG")
#edges = [ ("A", "B", 7), ("A", "D", 5),
#          ("B", "C", 8), ("B", "D", 9), ("B", "E", 7),
#	  ("C", "E", 5),
#	  ("D", "E", 15), ("D", "F", 6),
#	  ("E", "F", 8), ("E", "G", 9),
#	  ("F", "G", 11)]

g = prim( nodes, edges )

s2 = 0
for (a, b, w) in g:
    s2 += w

print s1/2-s2
f.close()

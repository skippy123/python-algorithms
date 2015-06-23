"""

A city's skyline is the outer contour of the silhouette formed by all the buildings in that city
when viewed from a distance. Now suppose you are given the locations and height of all the buildings
as shown on a cityscape photo (Figure A), write a program to output the skyline formed by these 
buildings collectively.


Sample input : [ [2 9 10], [3 7 15], [5 12 12], [15 20 10], [19 24 8] ] .
Sample output : [ [2 10], [3 15], [7 12], [12 0], [15 10], [20 8], [24, 0] ]



b = [ [2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8] ]

temp = []
left = [ [(k[0], k[2])]   for k in  b ]
right = [ [(k[1], k[2])]   for k in  b ]

points = left + right
sorted(points, key = lambda x:x[0])

import pdb;pdb.set_trace()
"""


def getSkyline(buildings):
    
    if len(buildings) == 0:
        return []
        
        
    l = []
    for b in buildings:
        l.extend( zip(xrange(b[0],b[1]+1), [b[2]]*(b[1]-b[0])) )
    
    m = {}
    for  i in l:
        
        if i[0] not in m:
            m[i[0]] = i[1]
        else:
            #import pdb; pdb.set_trace()
            m[i[0]] = max(i[1], m[i[0]])
    
    v = 0
    lb = buildings[0][0]
    ub = buildings[len(buildings)-1][1]
    
    res = []
    for k in xrange(lb, ub):
        if k in m:
            if m[k] != v:
                v = m[k]
                res.append([k,v])
        else:
            if v!= 0:
                v = 0
                res.append([k,v])
    res.append([ub, 0])

    return res


b = [ [2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8] ]
print getSkyline(b)



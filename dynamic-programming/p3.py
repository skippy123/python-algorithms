"""

Find all apths from cell  1,1 to m,n in matrix
Brute force is too easy which is recursive  , so try Dynamic Prog

"""

def numPaths(m, n):

    a = []
    

    for i in xrange(0, m):
            a.append([0]*(n))  

    for i in xrange(0, m):
        a[i][0] = 1

    for  j in xrange(0, n):
        a[0][j] = 1

    for  i in xrange(1 , m):
        for j in xrange(1 , n):
            a[i][j] = a[i-1][j] + a[i][j-1]
    
    #print a   
    return  a[m-1][n-1]

print numPaths(5,5)
print numPaths(4,3)   
print numPaths(3,3) 


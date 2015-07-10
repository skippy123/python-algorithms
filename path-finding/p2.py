"""
        Find all paths in a graph



def permute_string():
    s = "cat"

    res =[[]]

    for  i in xrange(0,len(s)):

        res = [ r+[j] for  r in res for j in s if j not in r ]

    print res

def print_values(node, x, y):

    if node is None:
        yield ''

    if node.val >  x and node.val < y:
        yield node
    else:
        return

    for  k  in print_values(node.left, x, y):
        yield k

    for k in print_values(node.right, x ,y):
        yield k

def p2(count):


    if count <= 20:
        yield count
    else:
        return 

    for k in  p2(count+1):
        yield k



#for k in  p2(10):
#    print k

def merge():

    a = [1, 2, 3, 4,4, 5]
    b = [4,5,6,7]
    c = []
    
    i = j = k= 0
 
    while ( i < len(a) and j < len(b) ):

        if a[i] > b[j]:
            c.append( b[j] )
            j += 1

        elif a[i] < b[j]:
            c.append( a[i])
            i += 1

        else:
            c.append( a[i])
            i += 1
            j += 1

        k += 1    

    while i <  len(a):
        c.append( a[i])
        i += 1
        k += 1

    while j < len(b):
        c.append( b[j] )
        j += 1
        k += 1

    print c

#merge()

"""

def paths(graph):

    stack = []
    stack.append(graph)

    path = []
    while stack:

        n = stack.pop()
        path = []
        path.append(graph)

        if not n.neighbors:
            print path
            path.pop()

        for  k in n.neighbors:
            stack.append(k)






































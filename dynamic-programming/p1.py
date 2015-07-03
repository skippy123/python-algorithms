"""
    
    given coins {3,5,10} give count  of all possibilites to make a sum of 20

    ex: 
    3,3,3,3,3,5
    5,5,5,5
    10,10
    10,5,5

    So answer is 4

"""

def count(n):

    table = [0]*(n+1)
    table[0] = 1

    import pdb; pdb.set_trace()
    for i in xrange(3, n+1):
        table[i] += table[i-3]
    
    for i in xrange(5, n+1):
        table[i] += table[i-5]

    for i in xrange(10, n+1):
        table[i] += table[i-10]

    return table[n]

print count(20)

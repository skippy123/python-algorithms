"""

Most inefficient way to print powersets of a set

whats a powerset 

for set s = ['1','2','3','4']
its all the subsets including the set iteself which is s and null set
"""

import itertools

s = ['1','2','3','4']

res1 = [[]]
for j1 in xrange(len(s)-1):
    res1 = [  list(set(r + [i])) for r in res1 for i in s if i not in  r]
    res1.sort()
    res1 = list(k for k,_ in itertools.groupby(res1))
    print res1
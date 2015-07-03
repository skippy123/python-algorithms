"""
Longest AP in a sorted array

Given a set of numbers, find the Length of the Longest Arithmetic Progression (LLAP) in it.

Examples:

set[] = {1, 7, 10, 15, 27, 29}
output = 3
The longest arithmetic progression is {1, 15, 29}

set[] = {5, 10, 15, 20, 25, 30}
output = 6
The whole set is in AP
For simplicity, we have assumed that the given set is sorted. We can always add a
 pre-processing step to first sort the set and then apply the below algorithms.

"""


def longest_ap(a):


    m  = { a[j]: ''  for j in xrange(0, len(a))}
    max_len = 0

    for  j in xrange(1, len(a)):

        i = j-1; k = j+1; flag = False
        cd = 0
        temp = 0

        while i >= 0  and  k < len(a):

            if a[i] + a[k] == 2*a[j]:
                flag = True
                cd = a[k] - a[j]
                temp += 3
                break

            elif a[i] + a[k] < 2*a[j]:
                k += 1
            else:
                i -= 1

        #import pdb;pdb.set_trace() 

        while flag and  k < len(a)-1:
            if  a[k+1] - a[k] == cd:   
                temp +=1
                k += 1
            else:                
                flag = not flag
        
        max_len = max( max_len , temp)


    return max_len

print longest_ap([1, 7, 10, 15, 27, 29])
print longest_ap([5, 10, 15, 20, 25, 30])
print longest_ap([1, 7, 10, 13, 14, 19])
print longest_ap([1, 7, 10, 13, 16, 19])
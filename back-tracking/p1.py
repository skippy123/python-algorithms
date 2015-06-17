#!/usr/bin/env python

"""
    Fill two instances of all numbers from 1 to n in a specific way

    Given a number n, create an array of size 2n such that the array contains 2 instances of every number from 1 to n, and the number of elements between two instances of a number i is equal to i. If such a configuration is not possible, then print the same.

    Examples:

    Input: n = 3
    Output: res[] = {3, 1, 2, 1, 3, 2}

    Input: n = 2
    Output: Not Possible

    Input: n = 4
    Output: res[] = {4, 1, 3, 1, 2, 4, 3, 2}

"""

def fillUtil(arr, curr, n):

    #All numbers are filled
    if (curr == 0):
        return True
    
    i=0
    while i < 2*n-curr-1:
        
        if arr[i] ==0 and arr[i+curr+1]==0:

            arr[i] = arr[i+curr+1] = curr
            if fillUtil(arr, curr-1 ,n):
                return True    

            # This lets u backtrack
            arr[i] = arr[i + curr+1] = 0

        i += 1
    
    return False

def fill(n):

    arr = [0]*2*n
    
    #import pdb; pdb.set_trace()
    if fillUtil(arr, n, n):
        print arr
    else:
        print "Not possible"

fill(3)
#import pdb;pdb.set_trace()
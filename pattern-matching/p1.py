#!/usr/bin/env python

"""

String matching where one string contains wildcard characters
Given two strings where first string may contain wild card characters and second string is a normal string. 
Write a function that returns true if the two strings match. The following are allowed wild card characters in first string.

* --> Matches with 0 or more instances of any character or set of characters.
? --> Matches with any one character.

"""

def match(a, pattern , si, pi):

    #We reach the end of both strings
    if si == len(a) and pi == len(pattern):
        return True

    if pattern[pi] == '*' and pi+1 < len(pattern) and si == len(a):
        return False

    if pattern[pi] =='?' or pattern[pi] == a[si]:
        return match(a, pattern, si+1, pi+1)

    if pattern[pi] == '*':
        t1 = t2 = False
        if pi+1 == len(pattern):
            t1 = True
        if si+1 < len(a):
            t2 = match(a, pattern, si+1, pi)
        return t1 or t2

    return False

#import pdb;pdb.set_trace()
if match("sk", "s*", 0, 0):
    print "is a match"

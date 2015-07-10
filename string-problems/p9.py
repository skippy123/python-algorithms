"""
    Given two strings str1 and str2, find the shortest string that has both str1 and str2 as subsequences.

Examples:

Input:   str1 = "geek",  str2 = "eke"
Output: "geeke"

Input:   str1 = "AGGTAB",  str2 = "GXTXAYB"
Output:  "AGXGTXAYB"

"""

#str1 = "geek" ;  str2 = "eke"
str1 = "AGGTAB"; str2 = "GXTXAYB"
m = len(str1) ; n = len(str2)

def rec_soln(m, n):

    if m ==0:  
        return n
    if n ==0: 
        return m

    if str1[m] == str2[n]:
        return 1 + rec_soln(m-1, n-1)

    return  1 + min( rec_soln(m-1, n) , rec_soln(m, n-1) )


def dynamic_soln():

    L = []
    temp = [0] * (n+1)

    for i in  xrange(0, m+1):
        L.append(temp)

    for  i in xrange(1, m+1):
        for j in xrange(1, n+1):

            if str1[i-1] == str2[j-1]:
                L[i][j] = 1 + L[i-1][j-1]
            else:
                L[i][j] = max (L[i][j-1] , L[i-1][j])

    print L[m][n]

dynamic_soln()
#print rec_soln(m-1, n-1) + 1

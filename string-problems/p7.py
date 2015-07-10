"""
    Longest  plaindromic substring in a string

"""

s = "eycaaraacyecbatabcdaabaad"
m = {}

def check_palindrome(s1):

    return all( s1[j] == s1[len(s1) -1 -j] for j in xrange(0, len(s1)/2) )


def disting_pals(i):


    if i == len(s):
        return

    j = i-1 ; k = i+1

    if i ==  0:
        j = 0

    if i == len(s) -1:
        k = i

    #if i == len(s)-2:
    #    import pdb;pdb.set_trace()

    while j >=0 and k < len(s):

        if check_palindrome( s[j: k+1] ):
            if s[j: k+1] not in m:
                m[ s[j: k+1] ] = ''
            j -= 1
            k += 1
        else:
            break    

    disting_pals(i+1)
    #disting_pals(i-1)


disting_pals(0)
print m

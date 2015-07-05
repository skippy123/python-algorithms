"""

A Dynamic programming version for N Queens Problem

"""


def check_conflict(i1,i2, j1,j2):

    # Same height
    if j1 == j2:
        return True

    # Diagnonal  conflict
    if  abs ( (j2-j1)/(i2-i1) ) == 1:
        return True

    return False

def slove_nq(n):

    table = [ 0 for i in xrange(0, n+1) ]


    i = 1
    while i >= 1 and i <= n :

        table[i] += 1
        if table[i] > n:
            i -= 1
            continue

        out_flag = True
        print table

        #import pdb ; pdb.set_trace()
        for j in  xrange(1, i):


            flag= False
            while table[i] < n:

                if check_conflict( i,j, table[i], table[j]):
                    table[i] += 1
                else:
                    flag = True
                    break

            out_flag &= flag

            if not flag:
                table[i] = 0
                i = i -1

        if out_flag :
            i += 1 

    return table

print slove_nq(4)
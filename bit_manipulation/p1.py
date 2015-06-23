"""

Reverse bits of a given 32 bits unsigned integer.

For example, given input 43261596 (represented in binary as 00000010100101000001111010011100), 
return 964176192 (represented in binary as 00111001011110000010100101000000).

"""


def  reverseBits (N) : 
    ans = 0 
    for i in range ( 32 ):
        ans = ans <<1 
        ans |= (N & 1) 
        N  = N>>1 
    return ans


def swapbits(N, i,j):
    l = (N >> i) &1 
    h = (N >> j) &1

    if l ^ h:
        N ^= ( (1 <<i) | (1 <<j) )
    return  

def  reverseBits1 (N) : 
    ans = 0 
    for i in range ( 32 ):
        N = swapbits(N,i, 32-i-1)
        #N = N >> 1
        #ans = ans <<1 
        #ans |= (N & 1) 
        #N  = N>>1 
    return N


print reverseBits(43261596)
print reverseBits1(43261596)


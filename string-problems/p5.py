"""
 takes a string a and a longer string b as arguments, and returns a list of indices to the permutations of a found in b.

Here are some assumptions about the input arguments.

All letters in a and b are capitalized.
len(a) < len(b)
Only letters that exist in a will appear in b. i.e. set(a) == set(b)
Duplicate letters are allowed in both a and b.
Example:

If a = "SLSQ" and b = "SQLSSQLSQ", then the result would look like:

result = [
[0,2,3,5],
[0,2,3,8],
[0,2,4,5],
[0,2,4,8],
[0,2,7,8],
[0,6,7,8],
[3,6,7,8],
[4,6,7,8]]
Another way of looking at it; I wrote out explicitly what the results of a recursive algorithm might look like for the example above. The numbers are the indices to the letters of b.

0123456789
SQLSSQLSQS      SLSQ
S LS Q      ->  0235
S LS    Q   ->  0238
S L SQ      ->  0245
S L S   Q   ->  0248
S L    SQ   ->  0278
S     LSQ   ->  0678
   S  LSQ   ->  3678
    S LSQ   ->  4678


"""

a = "SLSQ"
b = "SQLSSQLSQ"
B = zip(b, xrange(0,len(b)))

from itertools import combinations

def non_recursive_soln():
    res = []

    for i in combinations(B, 4):
        #import pdb; pdb.set_trace()
        bstr = "".join(map(lambda x:x[0], i))
        if a.__contains__(bstr):
            res.append(map(lambda x:x[1], i))

#for i in res:
#    print i
       

def recurse(a_str, b_str, ai=0, bi=0):

    if not a_str:
        return
    
    import pdb;pdb.set_trace()
    if ai < len(a_str):
        for i in range(bi, len(b_str)):
            if a_str[ai] == b_str[i]:
                for r in recurse(a_str, b_str, ai+1, i+1):
                    yield str(i) + r
    else:
        yield ''

print list(recurse(a, b))


















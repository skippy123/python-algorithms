"""

Searching for Patterns | Set 4 (A Naive Pattern Searching Question)
Question: We have discussed Naive String matching algorithm here. Consider a situation where all characters of pattern are different. 
Can we modify the original Naive String Matching algorithm so that it works better for these types of patterns. 
If we can, then what are the changes to original algorithm?

Solution: In the original Naive String matching algorithm , we always slide the pattern by 1.
When all characters of pattern are different, we can slide the pattern by more than 1. Let us see how can we do this. 
When a mismatch occurs after j matches, we know that the first character of pattern will not match the j matched characters because 
all characters of pattern are different. So we can always slide the pattern by j without missing any valid shifts. Following is the
modified code that is optimized for the special patterns.

"""


def search(arr, pattern):

    i =0

    while i <= len(arr) - len(pattern):
        found = True
        for j1,p1 in  enumerate(pattern):
            if  arr[i+j1] != p1:
                found = False
                break

        if found:
            print "patter found at index {0}".format(i)

        if j1 == 0: 
            i += 1
        else:
            i += j1

search("skippy boy is a good boy", "boy")
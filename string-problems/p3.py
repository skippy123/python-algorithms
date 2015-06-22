
"""
**Given a string  find the longest repeated sequence and print its starting index 
If there are multiple such  sub-strings , print all their indexes

s1 = "aabbbccdwwddd"
so print index 2 and 10 

"""



s1 = "aabbbccdwwddd"
i = 0
longest = 0
index_pos = -1
stash = -1
j1 = 0
m = {}

while i < len(s1)-1:
    
    flag = 0 
    #import pdb; pdb.set_trace() 
    for  j1 in xrange(i+1,len(s1)):
        
        if s1[i] == s1[j1] and  abs(j1-i) >= longest:
            if flag == 1:
                flag = 0
            if abs(j1-i) == longest:
                stash = index_pos
                #last index
                if stash not in m and j1 == len(s1)-1:
                    m[stash] = longest
                
                flag = 1
            longest = abs(j1-i)
            index_pos = i
        elif s1[i] != s1[j1]:
            if flag == 1:
                if stash not in m:
                    m[stash] = [longest]
            break
    #import pdb; pdb.set_trace()
    i = j1

#import pdb; pdb.set_trace()
print longest+1
print index_pos
print s1[index_pos: index_pos+longest+1]
print m.keys()
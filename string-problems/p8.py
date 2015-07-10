"""
        Given a string, find the longest substring having same characters
        E.g- Input:    abgetsdfffasw
        Output:   fff 
"""

s = "abgesssstsdfffasw"

s1 = range(0, len(s))

res = [[]]

for k in s1:
    res.append([k])
res = res[1:]

old_res = [] 
for k in s:

    res = [ r +[i] for r in  res for i in s1  if r[-1] + 1 == i and s[r[-1]] == s[i]  ]
    if res:
        old_res = res
    else:
        break
out = ''
for k in old_res:
    for k1 in k:
        out += s[k1]

#print out

def linear_sol():

    temp = s[0]
    head = tail = -1
    max_len = -1
    max_idx = (-1,-1)
    for k in xrange(1, len(s)):

        #if k ==8 : import pdb; pdb.set_trace()
        if temp == s[k]:

            if head == -1:
                head = k-1
            tail = k

        else:
            if tail + 1 - head > max_len and head != -1:
                max_len = tail+1 - head
                max_idx = (head, tail+1)

            head = -1
            tail = k

        temp = s[k]

    print s[max_idx[0]: max_idx[1]]
    print max_len

linear_sol()


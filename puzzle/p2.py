"""
    Flatten a linked list

"""

l = [ [1,2] , [3] , [4, [2,1,5]] , [[4],8,[9, [10, [[11]]]]]  ]
#print l

res = []
def flatten_list(l, res):

    if not l:
        return

    for k in l:

        if isinstance(k, list):
            flatten_list(k, res)
        else:
            res.append(k)

    return res

print flatten_list(l , res )


"""

The N Queen is the problem of placing N chess queens on an N X N chessboard so that no two queens attack each other.

The expected output is a binary matrix which has 1s for the blocks where queens are placed. For example following is 
the output matrix for above 4 queen solution.

              { 0,  1,  0,  0}
              { 0,  0,  0,  1}
              { 1,  0,  0,  0}
              { 0,  0,  1,  0}

"""


# A short but an effective solution
def soln1():

    from itertools import permutations
    n = 8
    cols = range(n)
    for  vec  in  permutations(cols):
        if n == len(set(vec[i]+i for i in cols )) \
             == len(set(vec[i]-i for i in cols)):
            print vec

#soln1()


BOARD_SIZE = 4
 
def under_attack(col, queens):
    return col in queens or \
           any(abs(col - x) == len(queens)-i for i,x in enumerate(queens))
 
def solve(n):
    solutions = [[]]
    for row in range(n):
        solutions = [solution+[i+1]
                       for solution in solutions
                       for i in range(BOARD_SIZE)
                       if not under_attack(i+1, solution)]

        #import pdb; pdb.set_trace()
    return solutions
 
for answer in solve(BOARD_SIZE): print(list(enumerate(answer, start=1)))


""" 
def solve(n):
    solutions = [[]]
    for row in range(n):
        solutions = (solution+[i+1]
                       for solution in solutions # first for clause is evaluated immediately,
                                                 # so "solutions" is correctly captured
                       for i in range(BOARD_SIZE)
                       if not under_attack(i+1, solution))
        import pdb;pdb.set_trace()
    return solutions
 

answers = solve(BOARD_SIZE)
#import pdb;pdb.set_trace()
while True:
    try:
        ans = next(answers)
        #print(list(enumerate(ans, start=1)))
    except Exception,e:
        break
"""

#first_answer = next(answers)
def firstn(n):
    num = 0
    while num < n:
        yield num
        num += 1
    
sum_of_first_n = sum(firstn(5))
#print sum_of_first_n





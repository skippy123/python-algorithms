"""

The text of question below is exactly given by Google interviewer. So they are owner of the text and I am just quoting them. I am not the author of the text below: 

Imagine a museum floor that looks like this: 

.#.G. 
..#.. 
G.... 
..#.. 

G == Museum Guard 
# == obstruction/impassable obstacle 
. == empty space 

Write a piece of code that will find the nearest guard for each open floor space. Diagonal moves are not allowed. The output should convey this information: 

2#1G1 
12#12 
G1223 
12#34 

You may choose how you want to receive the input and output. For example, you may use a 2-d array, as depicted here, or you may use a list of points with features, if you deem that easier to work with, as long as the same information is conveyed. 

"""

maze = [
  ['.', '#', '.', 'G', '.'],  
  ['.', '.', '#', '.', '.'],  
  ['G', '.', '.', '.', '.'],  
  ['.', '.', '#', '.', '.']  
    ]

x = [1,-1,0,0]
y = [0,0,-1,1]


def update_bfs_maze(i, j, value):

    queue = []
    queue.append((i,j))

    #import pdb; pdb.set_trace()
    while queue:

        temp_queue = []
        while queue:

            x_y = queue.pop(0)
            #get neighbours
            for  k in xrange(0, len(x)):
                next_x = x_y[0] + x[k]
                next_y = x_y[1] + y[k]

                if isSafe(next_x, next_y, value+1):
                    maze[next_x][next_y] = str(value+1)
                    temp_queue.append((next_x, next_y))
        
        queue = temp_queue
        value += 1

def isSafe(x,y,value):

    #global  maze
    if (x < 0 or x >= 4) or (y <0  or y >= 5):
        return False

    #print "{0} , {1}".format(x,y)

    if maze[x][y] == '#' or maze[x][y] == 'G':
        return False

    if maze[x][y] != '.' :
        if int(maze[x][y]) <= value : 
            return False

    return True

def update_maze(m,n,value):

    for  i in xrange(0,len(x)):

        next_x = m + x[i]
        next_y = n + y[i]

        if isSafe(next_x, next_y, value+1):
            maze[next_x][next_y] = str(value+1)
            update_maze(next_x, next_y, value+1)

def recursive_soln(): 
    for i  in  xrange(0,4):
        for j in range(0,5):
            if maze[i][j] == 'G':
                update_maze(i,j,0)

    print maze

def bfs_soln():

    for i  in  xrange(0,4):
        for j in range(0,5):
            if maze[i][j] == 'G':
                update_bfs_maze(i,j,0)


    print maze

bfs_soln()



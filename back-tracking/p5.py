"""
    Rat maze:

    A Maze is given as N*N binary matrix of blocks where source block is the upper left most block i.e.,
    maze[0][0] and destination block is lower rightmost block i.e., maze[N-1][N-1]. A rat starts from source 
    and has to reach destination. The rat can move only in two directions: forward and down.
    In the maze matrix, 0 means the block is dead end and 1 means the block can be used in the path from source
    to destination. Note that this is a simple version of the typical Maze problem. For example, a more 
    complex version can be that the rat can move in 4 directions and a more complex version can be with limited
    number of moves.

Following is an example maze.

"""

maze =  [   [1, 0, 0, 0],
            [1, 1, 1, 0],
            [0, 1, 0, 0],
            [1, 1, 1, 1]
        ]


def  print_path(maze, i, j, m, n, path):

    if i >= m or j >= n :
        return []

    if maze[i][j] == 0:
        return []

    if i == m-1 and j == n-1:
        path.append( (i,j) )
        return path

    path.append( (i,j) )

    #import pdb;pdb.set_trace()
    return  print_path(maze, i+1, j, m ,n, path) or print_path(maze, i, j+1, m ,n, path)

    #l2 = print_path(maze, i, j+1, m ,n, path)

    #return path

"""    
    if not l1 and not l2:
        return []

    if l1:
        return l1

    if l2:
        return l2
"""

print print_path(maze, 0,0,4,4, []) 


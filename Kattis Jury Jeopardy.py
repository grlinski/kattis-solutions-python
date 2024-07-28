

# Jury Jeopardy
# https://open.kattis.com/problems/juryjeopardy
# Works, is just too slow on Case2

import time,datetime


def reorient(ori,move):
    # Ori is n,e,s,w

    # So first change the orientation
    # If moving forward the orientation doesn't change
    if move == 'F':
        ori = ori

    # Backwards/Reverse
    elif move == 'B':
        if ori == 'n':
            ori = 's'
        elif ori == 's':
            ori = 'n'
        elif ori == 'e':
            ori = 'w'
        elif ori =='w':
            ori = 'e'

    # Turn Right
    elif move == 'R':
        if ori == 'n':
            ori = 'e'
        elif ori == 's':
            ori = 'w'
        elif ori == 'e':
            ori = 's'
        elif ori =='w':
            ori = 'n'


    # Turn Left
    elif move == 'L':
        if ori == 'n':
            ori = 'w'
        elif ori == 's':
            ori = 'e'
        elif ori == 'e':
            ori = 'n'
        elif ori == 'w':
            ori = 's'

    return ori




def movement(ori,x,y):
    # x =
    #

    q= []

    if ori == 'n':
        y-=1
    elif ori == 's':
        y+=1
    elif ori == 'e':
        x+=1
    elif ori == 'w':
        x-=1

    q.append(x)
    q.append(y)

    return q,x,y


# Finds the Size of the Maze
def maze_size(q):

    len1 = 0
    len2 = 0
    h1 = 0
    h2 = 0

    for i in q:
        x = i[0]
        y = i[1]

        len1 = min(len1,x)
        len2 = max(len2,x)
        h1 = min(h1, y)
        h2 = max(h2, y)

    #print(h2,h1)
    #print(len2,len1)

    h1 = (h2-h1)
    len1 = (len2-len1)


    return create_maze(len1,h1)

    #return len1,h1



def create_maze(leng,height):
    leng = leng+2
    height = height+2

    print(height+1,leng)

    maze = []


    for i in range(0,height):
        q = []
        for j in range(0,leng):
            q.append('#')
        maze.append(q)

    return maze


# Since the base coordinates may not start or end at 0,0
# Probably need to adjust data
def coordinate_correction(coord):
    lowx = 0
    lowy = 0

    for i in coord:
        x = i[0]
        y = i[1]
        lowx = min(x,lowx)
        lowy = min(y,lowy)

    adjx = abs(0-lowx)
    adjy = abs(0-lowy)

    for i in coord:
        i[0] = i[0]+adjx
        i[1] = i[1]+adjy

    return coord




def pathfinder(maze,coord):

    for i in coord:
        x = i[0]
        y = i[1]
        maze[y][x] = '.'

    return maze



def map_print(maze):

    # The top of the maze should be a row full of #
    # This is added here
    for i in range(len(maze[0])):
        print('#',end='')
    print()

    for i in maze:
        for j in i:
            print(j,end='')
        print()





t = int(input())
start = datetime.datetime.now()


print(t)
for i in range(t):
    x = 0
    y = 0
    coord = [[0,0]]
    s = input()

    # Orientation
    ori = 'e'
    for move in s:

        # Reorient, Works
        ori = reorient(ori,move)

        # Update Coordinates
        temp,x,y = movement(ori,x,y)
        coord.append(temp)

    coord = coordinate_correction(coord)

    maze = (maze_size(coord))
    maze = (pathfinder(maze,coord))

    map_print(maze)

end = datetime.datetime.now()
print(end-start)

#print(coord)






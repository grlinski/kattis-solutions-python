

# Jury Jeopardy Mk2
# https://open.kattis.com/problems/juryjeopardy
# Works, is just too slow on Case2


# Combine Functions into one

import time,datetime




def reorient_and_move(ori,move,x,y):
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


    # Movement
    q = []

    if ori == 'n':
        y -= 1
    elif ori == 's':
        y += 1
    elif ori == 'e':
        x += 1
    elif ori == 'w':
        x -= 1

    q.append(x)
    q.append(y)

    return q, x, y




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
    lowy = 0
    hiy = 0
    lowx = 0
    hix = 0

    for move in s:

        # Reorient and Move
        temp, x, y = reorient_and_move(ori,move,x,y)
        lowy = min(lowy,y)
        lowx = min(lowx,x)
        hiy = max(hiy,y)
        hix = max(hix,x)
        coord.append(temp)

    # Maze Size
    mx = (hix-lowx)
    my = (hiy-lowy)

    coord = coordinate_correction(coord)
    maze = create_maze(mx,my)

    maze = (pathfinder(maze,coord))

    map_print(maze)

end = datetime.datetime.now()
print(end-start)


#print(coord)






















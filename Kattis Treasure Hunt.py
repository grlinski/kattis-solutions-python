

# Treasure Hunt
# https://open.kattis.com/problems/treasurehunt




# Works but is too slow


r,c = map(int, input().split(' '))

maze = []
for i in range(r):
    s = input()
    q = []
    for j in s:
        q.append(j)

    maze.append(q)

coord = []

# List of Coordinates

for i in range(r):
    q = []
    for j in range(c):
        q = [i,j]
        coord.append(q)

x = 0
y = 0

count = 0
set1 = set()

while True:

    move = maze[x][y]
    pos = [x,y]

    if pos in coord:
        coord.remove(pos)
    elif pos not in coord:
        print('Lost')
        break


    if move == 'E':
        y+=1
    elif move == 'W':
        y-=1
    elif move == 'N':
        x-=1
    elif move == 'S':
        x+=1
    elif move == 'T':
        print(count)
        break

    if x < 0 or y < 0 or x >= c or y >= r:
        print('Out')
        break





    count+=1










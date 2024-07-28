
# Identifying Map Tiles
# https://open.kattis.com/problems/maptiles2


# Quadkey
"""
0 = top left
1 = top right
2 = bottom left
3 = bottom right



"""

r = 1
c = 1
x = 1
y = 1

# Note x,y offset by 1 each

s = input()
z = len(s)

for i in s:


    # Top/Bottom
    if i == '0' or i == '1':
        y = y*2-1

    else:
        y = y*2

    # Right Left
    # 0 and 2 are left
    if i == '0' or i == '2':
        x = x * 2 - 1

    else:
        x = x * 2

x=x-1
y=y-1

print(z,x,y)












# Dice Game
# https://open.kattis.com/problems/dicegame

ga1, gb1, ga2, gb2 = (map(int, input().strip().split(' ')))
ea1, eb1, ea2, eb2 = (map(int, input().strip().split(' ')))

gtotal = 0
gnum = 0
for i in range(ga1,gb1+1):
    for j in range(ga2,gb2+1):
        gtotal = gtotal+i+j
        gnum+=1

etotal = 0
enum = 0
for i in range(ea1, eb1 + 1):
    for j in range(ea2, eb2 + 1):
        etotal = etotal + i + j
        enum += 1

g = gtotal/gnum
e = etotal/enum

if g > e:
    print('Gunnar')
elif e > g:
    print('Emma')
else:
    print('Tie')







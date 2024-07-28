
# Number Fun
# https://open.kattis.com/problems/numberfun


times = int(input())

for i in range(times):
    x, y, z = map(int, input().split(' '))

    if x+y == z or x-y == z or x/y == z or x*y == z or y-x == z or y/x == z:
        print('Possible')
    else:
        print('Impossible')







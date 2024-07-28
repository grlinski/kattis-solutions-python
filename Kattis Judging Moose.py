
# Judging Moose
# https://open.kattis.com/problems/judgingmoose

x,y = map(int, input().split(' '))

if x == 0 and y == 0:
    print('Not a moose')
elif x != y:
    print('Odd',max(y,x)*2)
else:
    print('Even',max(y,x)*2)










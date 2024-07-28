# Railroads
# https://open.kattis.com/problems/railroad2

# Basically x have 4 outputs, and y has 3 outputs
# They need to balance out

x,y = map(int, input().split(' '))

a = x*4+y*3
if a%2 == 0:
    print('possible')
else:
    print('impossible')












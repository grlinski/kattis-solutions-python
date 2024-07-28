
# Tri
# https://open.kattis.com/problems/tri

import itertools


x,y,z, = (map(str, input().strip().split(' ')))
ops = ['+','*',"-",'/']

for i in range(0,4):
    op = ops[i]

    s=x+op+y
    r=y+op+z


    if int(eval(s)) == int(z):
        print(x+op+y+"="+z)
        break
    elif int(eval(r)) == int(x):
        print(x + "=" + y + op + z)
        break









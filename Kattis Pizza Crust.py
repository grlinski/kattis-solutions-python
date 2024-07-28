
# Pizza Crust
# https://open.kattis.com/problems/pizza2

import math

pi = math.pi

r,c = (map(int, input().strip().split(' ')))

pa = (r**2*pi)
#print(pa)

nr = c-r
npa = (nr**2*pi)
print((npa/pa)*100)







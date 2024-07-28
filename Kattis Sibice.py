

# Sibice
# https://open.kattis.com/problems/sibice

import math
n, w, h = map(int, input().split(' '))

d = (math.sqrt((w**2)+(h**2)))
for i in range(n):
    x = int(input())
    if x <= d:
        print('DA')
    else:
        print('NE')


















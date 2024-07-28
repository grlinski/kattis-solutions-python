
# Ladder
# https://open.kattis.com/problems/ladder
import math
h,d = map(int, input().split(' '))
x = math.sin(math.radians(d))
print(int(math.ceil(h/x)))













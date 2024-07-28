
# Statistics
# https://open.kattis.com/problems/statistics

# Great Example of my first Kattis submission that works via Sys

import sys

case = 1
for line in sys.stdin.readlines():
    x = list(map(int, line.strip().split(' ')))
    del(x[0])
    a = (min(x))
    b = (max(x))
    c = b-a

    print('Case ' + str(case)+': '+str(a) + " " + str(b) + ' ' + str(c))

    case+=1







# Original Code, used to actually see values

"""
case = 1
while True:
    x = list(map(int, input().strip().split(' ')))
    del(x[0])
    a = (min(x))
    b = (max(x))
    c = b-a

    print('Case ' + str(case)+': '+str(a) + " " + str(b) + ' ' + str(c))

    case+=1


"""























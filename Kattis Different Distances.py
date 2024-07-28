
# Different Distances
# https://open.kattis.com/problems/differentdistances

import math

while True:
    try:
        x1, y1, x2, y2, p = (map(float, input().strip().split(' ')))
    except:
        break


    d = ((abs(x1-x2)**p) + ((abs(y1-y2)**p)))**(1/p)

    print(d)


"""

Note Also must return to starting city

Try creating a naive solution
ie Brute Force
Then work from there


"""










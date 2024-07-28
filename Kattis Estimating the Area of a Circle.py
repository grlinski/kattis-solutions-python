
# Estimating the Area of a Circle
# https://open.kattis.com/problems/estimatingtheareaofacircle

import math
pi = math.pi


while True:

    r, c, m = (map(float, input().strip().split(' ')))

    if r == 0 and c== 0 and m == 0:
        break

    truearea = pi*(r**2)
    squarearea = (r*2)*(r*2)
    estimate = (m/c)*squarearea

    print(truearea,estimate)








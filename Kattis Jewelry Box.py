
# Jewelry Box
# https://open.kattis.com/problems/jewelrybox
# http://www.dummies.com/education/math/calculus/how-to-use-differentiation-to-calculate-the-maximum-volume-of-a-box/

import math


def qsolve(a,b,c):
    ans = []

    try:
        minus = ((-b)-math.sqrt((b**2)-(4*a*c)))/(2*a)
        ans.append(minus)
    except:
        pass

    try:
        plus = ((-b)+math.sqrt((b**2)-(4*a*c)))/(2*a)
        ans.append(plus)
    except:
        pass

    return ans




t = int(input())
for i in range(t):
    l, w = (map(int, input().strip().split(' ')))

    limit = min(l,w)
    limit = limit/2

    # Quadratic Equation Portions
    c = (l*w)
    b = ((-2*l)+(-2*w))*2
    a = 4*3

    qs = qsolve(a,b,c)



    for j in qs:
        if j >= limit or j <= 0:
            pass
        else:
            h = j

    # New A and B values, for length and width of box
    a = l-(2*h)
    b = w-(2*h)

    v = h*a*b
    print(v)


"""

v = L*W*H
a = L-2H
b = W-2H

v = (L-2H)*(W-2H)*H


v = l*w*h-2lh**2 - 2wh**2 + 4h**3 

h has to be between 0 and the lower of x and y divided by 2
set v to zero
0 = l*w*h-2lh**2 - 2wh**2 + 4h**3 
solve for h
remove each value
0 = l*w - 2l - 2w + 4h**2
2l + 2w - l*w = 4h**2 
sqrt(2l+2w-(l*w))/2 = h

Any number that falls in our range is good to go.



"""


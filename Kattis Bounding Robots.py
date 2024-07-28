
# Bounding Robots
# https://open.kattis.com/problems/boundingrobots

"""

So for this the robot thinks it's x,y coordinates are where it tries to move to
However where it actually is, is determined by the size of the rectangle w,l
If the width is 2 and the robot tries to move 5 to the right, it cannot because the width is too small.



"""



while True:
    w, l = map(int, input().split(' '))
    if w == 0 and l == 0:
        break

    robotx = 0
    roboty = 0

    actx = 0
    acty = 0

    n = int(input())


    # Robot Starts at 0,0

    for i in range(n):
        d,m = input().split()

        # Up and Right are Positive
        if d == 'u':
            roboty = roboty+int(m)

            if acty + int(m) >= l:
                acty = l-1
            else:
                acty = acty+int(m)

        elif d == 'r':
            robotx = robotx + int(m)

            if actx + int(m) >= w:
                actx = w-1
            else:
                actx = actx+int(m)


        elif d == 'd':
            roboty = roboty - int(m)

            if acty - int(m) <= 0:
                acty = 0
            else:
                acty = acty-int(m)


        elif d == 'l':
            robotx = robotx - int(m)

            if actx - int(m) <= 0:
                actx = 0
            else:
                actx = actx-int(m)




    print('Robot thinks',robotx,roboty)
    print('Actually at',actx,acty)
    print()



























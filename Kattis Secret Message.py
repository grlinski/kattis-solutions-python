


# Secret Message
# https://open.kattis.com/problems/secretmessage


import math


t = int(input())


def findsquare(x):

    y = int(math.sqrt(x))
    z = y**2
    if z == x:
        return y
    else:
        return y+1





def swap_row_col(x):

    row = len(x)
    col = len(x[0])
    y = []
    z = []

    for i in range(0,col):
        for j in range(0,row):
            a = x[j][i]
            y.append(a)
        z.append(y)
        y = []


    return z







for i in range(t):
    x = input()
    l = len(x)
    #Size
    s = (findsquare(l))

    dif = int(s**2-l)
    if dif !=0:
        x = x+'*'*dif



    q = []
    r = []

    for i in range(int(s**2)):
        r.append(x[i])
        if (i+1)%s == 0:
            q.append(r)
            r = []

    q = swap_row_col(q)
    print('asdsa')
    for i in range(0,len(q)):
        if q[i] == '*':
            pass
        else:
            print(q[i],end=' ')
    print()





















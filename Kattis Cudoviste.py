

# Cudoviste
# https://open.kattis.com/problems/cudoviste

# Note I was lazy and the code doesn't loop in a sensible order
# At least I think
# But it passes the tests


def countcars(a,b,c,d):
    count = 0
    if a == 'X':
        count+=1
    if b == 'X':
        count+=1
    if c == 'X':
        count+=1
    if d == 'X':
        count+=1
    return count



r,c = (map(int, input().strip().split(' ')))


q = []

zero = 0
one = 0
two = 0
three = 0
four = 0
cars = [0,0,0,0,0]



for i in range(r):
    q.append((input()))

for i in range(r-1):
    for j in range(c-1):

        # Car Dimensions, top,right,left,down, 2x2
        tl = q[i][j]
        tr = q[i][j+1]
        dl = q[i+1][j]
        dr = q[i+1][j+1]

        #Free Spot
        if tl == tr == dl == dr == '.':
            cars[0]+=1
        # No Spot
        elif tl == '#' or tr == '#' or dl =='#' or dr == '#':
            pass
        elif (tl == '.' or tl == 'X') or (tr == '.' or tr) (dl == '.' or dl) or (dr == '.' or dr):
            num = countcars(tl,tr,dr,dl)
            cars[num]+=1







for i in cars:
    print(i)


"""
# = Building
X = Parked Car
. = Free

Monster Truck = 2x2 spaces






"""







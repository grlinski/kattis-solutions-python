

# https://open.kattis.com/problems/encodedmessage
# Encoded Message



"""
Arrange Letters into a Square
Rotate Quarter Turn Clockwise




"""

# X is the string, l is the width and length of the square
def into_square(x,l):
    sq = []
    q = []
    l-1
    clean = 0
    for i in range(0,len(x),l):
        q =[]
        for j in range(i,i+l):
            q.append(x[j])
        sq.append(q)




    #print(sq)
    return sq




# Rotates the Square Counter Clockwise
def rotate_ccw(x,l):
    # Basically the last column becomes the first row and so on

    ns = ""
    l = l-1

    for c in range(l,-1,-1):
        for r in range(0, l+1):
            ns = ns+x[r][c]

    print(ns)





times = int(input())

for i in range(times):
    s = input()
    l = len(s)
    length = int(l**(1/2))
    #print(s)
    #print(length)

    # Returns List X, which is a square version of s
    x = into_square(s,length)

    # Rotates the X square and returns as a list
    y = rotate_ccw(x,length)



"""

1
RSTEEOTCP

"""




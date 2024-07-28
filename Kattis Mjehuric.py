


# Mjehuric
# https://open.kattis.com/problems/mjehuric


"""
Rules

If # on 1st greater than 2nd swap
If # on 2nd


"""

aseq = [1,2,3,4,5]


x = list(map(int, input().strip().split(' ')))


swap = False

while x != aseq:
    for i in range(0,len(x)-1):
        if x[i] > x[i+1]:
            hold = x[i]
            x[i] = x[i+1]
            x[i+1] = hold
            swap = True
        else:
            swap = False
        if swap == True:
            for j in x:
                print(j,end=' ')
            print()





    #if x == aseq:
     #   break
























# Kattis Prsteni
# https://open.kattis.com/problems/prsteni


def GCD(x,y):
    #if x%y == 0:
    #    return x//y, 1
    #elif y%x == 0:
    #    return 1, y//x

    a = x
    b = y
    while a != b:
        if a > b:
            a = a-b
        else:
            b = b-a
    return x//a,y//a










t = int(input())

q = list(map(int, input().strip().split(' ')))






init = q[0]
for i in range(t-1):
    current = q[i+1]
    numer,denom = GCD(init,current)
    print(str(numer)+"/"+str(denom))





















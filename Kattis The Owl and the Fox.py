


# The Owl and the Fox
# https://open.kattis.com/problems/owlandfox



def backwards(x):
    nx = ''
    downone = False
    for i in range(len(x)-1,-1,-1):
        a = x[i]
        if a == '0':
            nx=a+nx
        elif downone == False:
            b = int(a)-1
            a = str(b)
            nx = a + nx
            downone = True
        else:
            nx = a + nx
    return nx




t = int(input())

for i in range(t):
    x = input()
    print(int((backwards(x))))














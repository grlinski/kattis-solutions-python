
# Yoda
# https://open.kattis.com/problems/yoda




x = input()
y = input()


if len(x) == len(y):
    pass
elif len(x) > len(y):
    dif = len(x)-len(y)
    y = ('0'*dif)+y
else:
    dif = len(y)-len(x)
    x = ('0'*dif)+x


nx = ''
ny = ''

# If x or y lose all their numbers print YODA
# This checks if they lose any.
xkept = False
ykept = False


for i in range(len(x)-1,-1,-1):
    a = int(x[i])
    b = int(y[i])

    if a == b:
        nx = x[i] + nx
        ny = y[i] + ny
        xkept = True
        ykept = True


    elif a > b:
        nx = x[i] + nx
        xkept = True
    elif b > a:
        ny = y[i] + ny
        ykept = True


if len(nx) == 0:
    print('YODA')
else:
    print(int(nx))

if len(ny) == 0:
    print('YODA')
else:
    print(int(ny))











# Cetvrta

# https://open.kattis.com/problems/cetvrta
# Do with paper


# Rectangle Not Square
# Abs diff not needed

x = []
y = []

for i in range(3):
    a,b = map(int, input().split(' '))
    x.append(a)
    y.append(b)



# Find the non matching value in x and y
x.sort()
y.sort()
if x[0]==x[1]:
    ax = x[2]
else:
    ax = x[0]

if y[0]==y[1]:
    ay = y[2]
else:
    ay = y[0]


print(ax,ay)

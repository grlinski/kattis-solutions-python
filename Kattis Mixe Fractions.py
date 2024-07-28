


# Mixed Fractions
# https://open.kattis.com/problems/mixedfractions

while True:
    x, y = (map(int, input().strip().split(' ')))
    if x ==0  and y ==0:
        break

    rem = x%y
    num = x//y
    print(num,rem,"/",y)














# Parking
# https://open.kattis.com/problems/parking2




times = int(input())

for i in range(times):
    stores = int(input())
    q = list(map(int, input().strip().split(' ')))
    mini = min(q)
    maxi = max(q)
    total = (maxi-mini)*2

    print(total)












"""

1
4
24 13 89 37

1
6
7 30 41 14 39 42


"""





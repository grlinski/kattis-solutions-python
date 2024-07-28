


# Army Strength Easy
# https://open.kattis.com/problems/armystrengtheasy




t = int(input())

for i in range(t):
    b = input()
    ng,nm = map(int, input().split(' '))

    sg = list(map(int, input().strip().split(' ')))
    sm = list(map(int, input().strip().split(' ')))
    maxg = max(sg)
    maxm = max(sm)

    if maxg >= maxm:
        print('Godzilla')
    else:
        print('MechaGodzilla')















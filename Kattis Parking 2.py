

# Parking, the 1.5 difficulty one
# https://open.kattis.com/problems/parking



a,b,c = (map(int, input().strip().split(' ')))

ar = []
de = []
cost = [a,b,c]
parked = [0,0,0]

for i in range(3):
    x,y = (map(int, input().strip().split(' ')))
    ar.append(x)
    de.append(y)

total = 0

for j in range(min(ar),max(de)+1):
    if j >= ar[0] and j < de[0]:
        parked[0] = 1
    else:
        parked[0] = 0

    if j >= ar[1] and j < de[1]:
        parked[1] = 1
    else:
        parked[1] = 0

    if j >= ar[2] and j < de[2]:
        parked[2] = 1
    else:
        parked[2] = 0

    p = sum(parked)
    total = total + cost[p-1]*p

    #print('Time, Parked, Cost Per, Cost')
    #print(j,p,cost[p-1],cost[p-1]*p)


print(total)







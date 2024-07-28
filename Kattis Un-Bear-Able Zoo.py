

# Unbearable Zoo
# https://open.kattis.com/problems/zoo




listnum = 1

while True:
    n = int(input())
    animals = {}
    aniset = set()
    ans = []

    if n ==0:
        break
    for i in range(n):
        j = input().split()
        ani = j[-1].lower()
        aniset.add(ani)

        if ani not in animals:
            animals[ani] = 1
        else:
            z = animals[ani]+1
            animals[ani] = z

    for i in animals:
        x = i + ' | ' +str(animals[i])
        ans.append(x)
    ans.sort()

    print('List '+ str(listnum) + ':')
    for i in ans:
        print(i)
    listnum+=1














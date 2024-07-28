

# What Does the Fox Say

# https://open.kattis.com/problems/whatdoesthefoxsay



t = int(input())

for i in range(t):
    mainsay = input().split()
    rem = []
    while True:
        x = input().split()
        if x[0] == 'what':
            break
        rem.append(x[2])

    while len(rem) != 0:
        if rem[0] in mainsay:
            mainsay.remove(rem[0])
        elif rem[0] not in mainsay:
            del(rem[0])

    for j in mainsay:
        print(j,end = ' ')
    print()




















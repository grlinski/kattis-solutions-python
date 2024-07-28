

# Line Them Up
# https://open.kattis.com/problems/lineup


times = int(input())

q = []
ao = True
do = True

def checker(new,prev):
    score = 0

    doc = True
    aoc = True
    mini = min(len(new),len(prev))


    for i in range(1,mini):
        x = ord(new[i])
        y = ord(prev[i])
        if x==y:
            pass
        elif x > y:
            doc = False
            break
        elif y < x:
            aoc = False
            break

    if doc == True and aoc == True:
        if len(new) > len(prev):
            doc = False
        else:
            aoc = False

    return aoc,doc



alreadyprinted = False
x = input()
pname = x
pfl = x[0]

for i in range(times-1):
    x = input()

    nfl = x[0]
    name = x

    if ord(nfl) > ord(pfl):
        do = False
    elif ord(nfl) < ord(pfl):
        ao = False
    elif name == pname:
        pass
    elif ord(nfl) == ord(pfl):
        a1,d1 = checker(name,pname)
        if a1 == False:
            ao = False
        if d1 == False:
            do = False


    pfl = nfl
    pname = name






if ao == False and do == False and alreadyprinted == False:
    print('NEITHER')
elif ao == True and do == False:
    print('INCREASING')
elif ao == False and do == True:
    print('DECREASING')

#print(do,ao)







"""



Increasing

8
A
AA
AAA
AAAA
AAAA
AAAA
AAAAA
B


Decreasing

6
ZZZZZ
Z
W
K
G
A


Neither
6
ZZZZZ
Z
W
Z
K
G
A




"""








# Synchronizing Lists
# https://open.kattis.com/problems/synchronizinglists


# Mk1 Works AFAIK

# Mk2 Is so I can expand M1 without losing everything in case I screw up

while True:
    items = int(input())
    if items == 0:
        break

    m = []
    list1 = []
    list2 = []
    sort1 = []
    sort2 = []

    total1 = 0
    total2 = 0

    # List Creator 1
    for i in range(items):
        x = int(input())
        sort1.append(x)
        total1 = total1 + x

    # List Creator 2
    for i in range(items):
        x = int(input())
        list2.append(x)
        total2 = total2 + x

    # Sort List 1
    list1 = sort1[::]
    sort1.sort()

    # Compare Positions Between Lists
    move = []
    for i in range(0, len(sort1)):
        x = sort1[i]
        indy = list1.index(x)
        diff = indy - i
        move.append(diff)

    # Sort List 2
    sort2 = list2[::]
    sort2.sort()

    #print(move)
    #print(list1)
    #print(sort1)

    #print()

    #print(list2)
    #print(sort2)
    #print(move)
    # 6 55 73 10

    # Apply Move to sort 2
    for i in range(0, len(sort2)):
        change = move[i] + i
        #print(change)

        list2[change] = sort2[i]

    for i in list2:
        print(i)

    print()


















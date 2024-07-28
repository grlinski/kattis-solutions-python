


# Mirror Images

# https://open.kattis.com/problems/mirror



times = int(input())

for i in range(times):
    r, c = map(int, input().split(' '))
    print("Test",i+1)
    list1 = []
    for j in range(0,r):
        s = input()
        q = s[::-1]
        list1.append(q)
    list2 = list1[::-1]
    for j in range(0,r):
        print(list2[j])







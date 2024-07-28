

# Stand on Zanzibar
# https://open.kattis.com/problems/zanzibar


times = int(input())

for i in range(times):
    q = input().split()
    total = 0

    for j in range(1,len(q)):
        x = int(q[j])
        y = int(q[j-1])
        if x == 0:
            break
        if x > y*2:
            total = total + (x)-(y*2)
    print(total)


















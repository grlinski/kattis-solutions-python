
# Server
# https://open.kattis.com/problems/server


items,time = map(int, input().split(' '))

q = list(map(int, input().strip().split(' ')))

total = 0
num = 0
for i in q:
    total = total+i
    if total > time:
        break
    else:
        num+=1

print(num)








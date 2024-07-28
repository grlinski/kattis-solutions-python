

# Soylent
# https://open.kattis.com/problems/soylent

times = int(input())


for i in range(times):
    total = 0
    x = int(input())

    y = x%400
    total = x//400
    if y!= 0:
        total+=1
    print(total)











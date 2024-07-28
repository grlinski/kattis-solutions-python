

# Planina
# https://open.kattis.com/problems/planina


times = int(input())

num = 2
if times == 0:
    print(4)
else:
    gap = 1
    for i in range(0,times):
        num = num+gap
        gap=gap*2
    print(num*num)









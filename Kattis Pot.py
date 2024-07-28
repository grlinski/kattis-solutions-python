

# Pot
# https://open.kattis.com/problems/pot

items = int(input())

total = 0
for i in range(0,items):
    q = input()
    num = int(q[:-1])
    exp = int(q[-1])
    total = total+num**exp

print(total)










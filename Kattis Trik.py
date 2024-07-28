


# Trik
# https://open.kattis.com/problems/trik




s = input()
cups = [1,0,0]
for i in s:
    if i == "A":
        hold = cups[0]
        cups[0] = cups[1]
        cups[1] = hold
    elif i == 'B':
        hold = cups[1]
        cups[1] = cups[2]
        cups[2] = hold
    elif i == 'C':
        hold = cups[0]
        cups[0] = cups[2]
        cups[2] = hold

for i in range(0,len(cups)):
    if cups[i] ==1:
        print(i+1)




















# Ragged Right
# https://open.kattis.com/problems/raggedright

import sys

mini = 100
maxi = 0
total = 0
q = []

for line in sys.stdin.readlines():
    x = input()
    q.append(len(x))
    maxi = max(maxi,len(x))


for i in range(0,len(q)-1):
    total += (maxi-q[i])**2

print(total)










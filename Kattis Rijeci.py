

# Rijeci
# https://open.kattis.com/problems/rijeci

x = int(input())

# Moves in a fibbo pattern

s = 'a'

leader = 1
lagger = 0
holder = 1

x = x-1
for i in range(x):
    #print(leader)
    holder = leader
    leader = leader+lagger
    lagger = holder



if x == -1:
    print(1,0)
else:
    print(lagger, leader)

"""
Original Brute Force Method
Shows all numbers

for i in range(x):
    ns = ""
    for j in s:
        if j == 'a':
            ns = ns+'b'
        else:
            ns = ns+'ba'
    s = ns
    b = 0
    a = 0
    for k in s:
        if k == 'a':
            a += 1
        else:
            b += 1

    print(a, b)

"""



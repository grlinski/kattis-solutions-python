

# Quality Adjusted Life Year
# https://open.kattis.com/problems/qaly
#

t = int(input())

total = 0
for i in range(t):
    a, b = map(float, input().split(' '))


    total += a*b

print(round(total,4))

















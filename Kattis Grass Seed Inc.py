

# Grass Seed Inc
# https://open.kattis.com/problems/grassseed


cost = float(input())
yards = int(input())
total = 0
for i in range(yards):
    w,l = map(float, input().split(' '))
    size = w*l*cost
    total = total+size

print(total)




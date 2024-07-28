
# Pet
# https://open.kattis.com/problems/pet

maxi = 0
i = 0
for i in range(5):
    s = list(map(int, input().strip().split(' ')))
    q = sum(s)
    if q>maxi:
        maxi = q
        num = i+1
print(num,maxi)



items = int(input())
s = list(map(int, input().strip().split(' ')))
"""
-1 walks
0
1
2
3
4


"""
atbats = len(s)
total = 0
for i in s:
    if i == -1:
        atbats-=1
    else:
        total=total+i

print(total/atbats)




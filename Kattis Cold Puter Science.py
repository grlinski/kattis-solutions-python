
# Cold-puter Science
# https://open.kattis.com/problems/cold


temps = int(input())
s = list(map(int, input().strip().split(' ')))

lessthan = 0
for i in s:
    if i < 0:
        lessthan+=1
print(lessthan)














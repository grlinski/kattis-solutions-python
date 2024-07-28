

# Dice Cup
# https://open.kattis.com/problems/dicecup
a,b = map(int, input().split(' '))

highest = a+b
q = [0]*(highest)

for i in range(0,a):
    for j in range(b):
        q[i+j]+=1
maxi = max(q)
for i in range(0,len(q)):
    if q[i] == maxi:
        print(i+2)






# Heir's Dilemma
# https://open.kattis.com/problems/heirsdilemma
import datetime






def numSplit(x):
    s = str(x)
    q = set()
    for i in s:
        q.add(int(i))

    if len(q) <6:
        return 0

    for i in q:


        if i==0:
            return 0
        elif x%i == 0:
            pass
        else:
            return 0

    return 1



t,b = map(int, input().split(' '))

start = datetime.datetime.now()

total = 0

if t%2==0:
    pass
else:
    t+=1
old = 0

for i in range(t,b+1,2):
    ld = int(str(i)[-1])


    if ld == 1 or ld == 3 or ld == 5 or ld == 7 or ld == 9 or ld == 0:
        pass
    elif '5' in str(i):
        pass
    else:
        j = numSplit(i)
        total+=j

print(total)
end = datetime.datetime.now()-start
print(end)

# 248
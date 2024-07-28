


# Ragged Right
# https://open.kattis.com/problems/raggedright


mini = 100
maxi = 0
total = 0
q = []

while True:
    x = input()
    if '.' in x:
        maxi = max(maxi, len(x))
        break
    else:
        q.append(len(x))
        maxi = max(maxi,len(x))


for i in range(0,len(q)):
    total += (maxi-q[i])**2

print(total)









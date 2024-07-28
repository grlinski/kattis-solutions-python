

# Zamka
# https://open.kattis.com/problems/zamka



def intsum(x):
    s = str(x)
    total = 0
    for i in s:
        total = total+int(i)
    return total






l = int(input())
d = int(input())
x = int(input())
q = []

# n = min
# m = max


for i in range(l,d+1):
    j = intsum(i)
    if j == x:
        q.append(i)


print(q[0])
print(q[-1])





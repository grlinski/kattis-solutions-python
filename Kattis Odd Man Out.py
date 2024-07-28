

# Odd Man Out
# https://open.kattis.com/problems/oddmanout



times = int(input())


for i in range(times):
    dis = int(input())
    q = list(map(int, input().strip().split(' ')))
    s = set(q)

    for j in s:
        r = q
        r.remove(j)
        if j not in r:
            print('Case #'+str(i+1)+":",j)
















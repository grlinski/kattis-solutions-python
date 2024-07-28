

# Popular Vote
# https://open.kattis.com/problems/vote



t = int(input())


for i in range(t):

    n = int(input())
    q = []
    for j in range(n):
        x = int(input())
        q.append(x)

    total = sum(q)
    half = total//2

    qsort = []
    for w in q:
        qsort.append(w)
    qsort.sort()


    if qsort[-1] == qsort[-2]:
        print('no winner')
    elif qsort[-1] > half:
        x = q.index(qsort[-1])+1
        print('majority winner',x)
    else:
        x = q.index(qsort[-1])+1
        print('minority winner', x)

















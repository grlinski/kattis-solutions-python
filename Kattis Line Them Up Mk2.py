



# Line Them Up
# https://open.kattis.com/problems/lineup


times = int(input())

q = []
ao = True
do = True


def name_score(x):

    score = 0
    for i in range(0,len(x)):
        y = ord(x[i])-64
        score = score+(y*10**(i+1))


    return score




for i in range(times):
    x = input()
    s = name_score(x)
    q.append(x)

a = q[::]
a.sort()
d = a[::-1]


#print(a)
#print(d)
#print(q)

if q == a:
    print('INCREASING')
elif q == d:
    print('DECREASING')
else:
    print('NEITHER')





"""



Increasing

8
A
AA
AAA
AAAA
AAAA
AAAA
AAAAA
B


Decreasing

6
ZZZZZ
Z
W
K
G
A


Neither
6
ZZZZZ
Z
W
Z
K
G
A




"""


















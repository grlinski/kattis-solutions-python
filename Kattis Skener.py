
# Skener

R,C,Zr,Zc = map(int, input().split(' '))

q = []
for i in range(0,R):
    s = input()
    q.append(s)


for i in range(0,len(q)):
    for k in range(0,Zr):
        for j in q[i]:
            print (j*Zc,end="")
        print()





"""

3 3 2 2
.x.
x.x
.x.

"""
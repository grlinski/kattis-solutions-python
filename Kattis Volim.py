
# Volim
# https://open.kattis.com/problems/volim





f = int(input())
ques = int(input())


q = []
for i in range(ques):
    x,y = input().split()
    q.append([int(x),y])




time = 0

f = f
for i in range(len(q)):
    x = q[i][0]
    y = q[i][1]


    time = time+x

    print('Pos, Time, Ans')
    print(f,time,y)

    if time >= 210:
        break

    if y != 'T':
        pass
    else:
        f+=1
        if f > 8:
            f = 1



print(f)







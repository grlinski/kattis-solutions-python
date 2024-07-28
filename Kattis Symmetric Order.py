
# Symmetric Order
# https://open.kattis.com/problems/symmetricorder

num = 1
while True:
    s = int(input())
    if s == 0:
        break
    q = []
    print('SET',num)
    num+=1

    for i in range(s):
        x = input()
        q.append(x)

    front = []
    back = []
    for i in range(0,len(q)):
        # Either insert or Append
        # Front first then back
        if i%2 == 0:
            front.append(q[i])
        else:
            back.append(q[i])


    ans = front + back[::-1]
    for j in ans:
        print(j)



































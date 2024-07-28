

# ACM Scoring Contest
# https://open.kattis.com/problems/acm


right = []
wrong = {}

total = 0


while True:
    q = input().split()
    #print(q)
    if len(q) == 1:
        break


    time = int(q[0])
    prob = q[1]
    rw = q[2]

    if prob in right:
        pass
    elif prob in wrong and rw == 'wrong':
        x = wrong[prob]+20
        wrong[prob] = x
    elif prob in wrong and rw == 'right':
        x = wrong[prob]
        total = total + time+x
        right.append(prob)
    elif rw == 'wrong':
        wrong[prob] = 20
    elif rw == 'right':
        right.append(prob)
        total = total+time
amount = len(right)
print(amount,total)








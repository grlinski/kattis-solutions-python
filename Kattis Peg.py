
# Peg
# https://open.kattis.com/problems/peg


q = []
q.append('xxxxxxxxxxx')
q.append('xxxxxxxxxxx')

for t in range(7):
    s = input()
    ns = s.replace(" ",'x')
    ns = "xx" + ns + 'xx'
    q.append(ns)
#q.append(['x','x','x','x','x','x','x'])
q.append('xxxxxxxxxxx')
q.append('xxxxxxxxxxx')

total = 0
for r in range(0,len(q)):
    for c in range(len(q[r])):
        x = q[r][c]

        if x == 'o':
            lx1 = q[r][c-1]
            lx2 = q[r][c - 2]

            rx1 = q[r][c+1]
            rx2 = q[r][c + 2]

            xu1 = q[r-1][c]
            xu2 = q[r-2][c]

            xd1 = q[r + 1][c]
            xd2 = q[r + 2][c]

            if lx1== 'o' and lx2 == '.':
                total+=1


            if rx1 == 'o' and rx2 == '.' and x=='o':
                total += 1


            if xu1== 'o' and xu2 == '.':
                total+=1


            if xd1 == 'o' and xd2 == '.':
                 total += 1


#print(q)
print(total)

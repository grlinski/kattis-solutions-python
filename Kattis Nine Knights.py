
# Nine Knights
# https://open.kattis.com/problems/nineknights

q =[]

q.append('.........')
q.append('.........')
for i in range(5):
    s = input()
    s = '..'+s+'..'
    q.append(s)


q.append('.........')
q.append('.........')

valid = True
kcount = 0


for r in range(7):
    for c in range(9):
        x = q[r][c]
        #print(x)
        if x == 'k':
            kcount+=1

            uur = q[r+2][c+1]
            uul = q[r+2][c-1]
            rru = q[r+1][c+2]
            rrd = q[r-1][c+2]
            ddr = q[r-2][c+1]
            ddl = q[r-2][c-1]
            lld = q[r-1][c-2]
            llu = q[r+1][c-2]

            #print(ddl)

            if (uur== 'k' or uul == 'k'or rru == 'k'or rrd == 'k'or ddr == 'k'or ddl== 'k' or lld == 'k'or llu== 'k') :
                valid = False
                break



if valid == True and kcount==9:
    print('valid')
else:
    print('invalid')


#print(q)

#

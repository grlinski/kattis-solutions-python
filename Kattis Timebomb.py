

# Timebomb

# https://open.kattis.com/problems/timebomb

zero = ['***','* *','* *','* *','***']
one = ['  *','  *','  *','  *','  *']
two = ['***','  *','***','*  ','***']
three = ['***','  *','***','  *','***']
four = ['* *','* *','***','  *','  *']
five = ['***','*  ','***','  *','***']
six = ['***','*  ','***','* *','***']
seven = ['***','  *','  *','  *','  *']
eight = ['***','* *','***','* *','***']
nine = ['***','* *','***','  *','***']

nums = [zero,one,two,three,four,five,six,seven,eight,nine]



def number(st,q):
    num = []
    for i in range(0,5):
        x = q[i]
        y = x[st:st+3]
        num.append(y)
    return num






q = []
while len(q) != 5:
    x = input()
    q.append(x)



length = len(q[0])
ans = ''
for i in range(0,length,4):
    x = number(i,q)
    if x == zero:
        ans = ans+'0'
    elif x == one:
        ans = ans + '1'
    elif x == two:
        ans = ans + '2'
    elif x == three:
        ans = ans + '3'
    elif x == four:
        ans = ans + '4'
    elif x == five:
        ans = ans + '5'
    elif x == six:
        ans = ans + '6'
    elif x == seven:
        ans = ans + '7'
    elif x == eight:
        ans = ans + '8'
    elif x == nine:
        ans = ans + '9'

numans = int(ans)
if numans%6 == 0:
    print('BEER!!')
else:
    print('BOOM!!')

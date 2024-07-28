
# Seven Wonders
# https://open.kattis.com/problems/sevenwonders


import datetime

start = datetime.datetime.now()

s = input()


start = datetime.datetime.now()

t = 0
c = 0
g = 0

for i in s:
    if i == 'T':
        t+=1
    elif i == 'G':
        g+=1
    elif i == 'C':
        c+=1



total = (t**2+g**2+c**2)

#print(t,g,c)
while True:
    if t > 0 and g > 0 and c >0:
        total = total +7
        c-=1
        g-=1
        t-=1
    else:
        break



print(total)
#end = datetime.datetime.now()
#print(start-end)











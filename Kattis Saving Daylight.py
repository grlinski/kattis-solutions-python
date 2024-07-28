
# Saving Daylight

# https://open.kattis.com/problems/savingdaylight


import sys,re
num = re.compile(r'\d*')
for line in sys.stdin.readlines():
    x = line.split()
    time1 = num.findall(x[3])
    h1 = int(time1[0])
    m1 = int(time1[2])

    time2 = num.findall(x[4])
    h2 = int(time2[0])
    m2 = int(time2[2])



    h3 = h2-h1

    if m1 > m2:
        m3 = m2-m1+60
        h3-=1
    else:
        m3 = m2-m1

    print(x[0],x[1],x[2],h3,'hours',m3,'minutes')





"""




import sys,re
num = re.compile(r'\d*')
while True:
    x = input().split()
    time1 = num.findall(x[3])
    h1 = int(time1[0])
    m1 = int(time1[2])

    time2 = num.findall(x[4])
    h2 = int(time2[0])
    m2 = int(time2[2])



    h3 = h2-h1

    if m1 > m2:
        m3 = m2-m1+60
        h3-=1
    else:
        m3 = m2-m1

    print(x[0],x[1],x[2],h3,'hours',m3,'minutes')















"""


















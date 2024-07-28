

# Help a PhD Candidate Out
# https://open.kattis.com/problems/helpaphd

import re
digit = re.compile(r'\d+')


times = int(input())

for i in range(times):
    s = input()
    q = digit.findall(s)
    #print(q)
    if len(q) == 0:
        print('Skipped')
    else:
        x = int(q[0])
        y = int(q[1])
        print(x+y)











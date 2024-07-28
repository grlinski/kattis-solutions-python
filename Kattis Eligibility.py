

import re

# Bad Question In My Opinion




t = int(input())

for i in range(t):
    s = input().split()

    x = s[2]
    by = int(x[:4])

    x = s[1]
    sy = int(x[:4])

    cred = int(s[3])

    eli = False

    if by >= 1991:
        eli = True
    elif sy >= 2010:
        eli = True
    elif cred >= 41:
        eli = False

    if 'Petition' in  s[0]:
        prt = 'coach petitions'
    elif eli:
        prt = 'eligible'
    else:
        prt = 'ineligible'



    print(s[0],prt)




"""
Eligibile if
Began studies in 2010 or later
Born in 1991 or later

Not Eligible if
Completed 8 semesters of full-time study
Which is 41 courses or more

1
EligibleContestant 2013/09/01 1995/03/12 10

format
Name Start Birth Courses


"""







# Datum
# https://open.kattis.com/problems/datum

d,m = map(int, input().split(' '))

# 1,1 == Thursday

cal = [31,28,31,30,31,30,31,31,30,31,30,31]
day = ['Wednesday','Thursday','Friday','Saturday','Sunday','Monday','Tuesday']


total = d
for i in range(0,m-1):
    total = total+cal[i]


ans = total%7
print(day[ans])






"""
Jan 31
Feb 28
Mar 31




"""







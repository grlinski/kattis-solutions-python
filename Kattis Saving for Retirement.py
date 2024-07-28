

# Saving for Retirement
# https://open.kattis.com/problems/savingforretirement

b1,b2,bm,a1,am = map(int, input().split(' '))



bd = b2-b1
bt = bd*bm

years = 0
total = 0

while total <= bt:
    total = total+am
    years+=1

print(a1+years)








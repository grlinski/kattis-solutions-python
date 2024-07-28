

# One Chicken Per Person
# https://open.kattis.com/problems/onechicken


peo,chk = map(int, input().split(' '))

enough = chk-peo
more = abs(peo-chk)

#print(enough)
#print(more)

if enough == 1:
    print('Dr. Chaz will have 1 piece of chicken left over!')
elif enough > 0:
    print('Dr. Chaz will have', enough, 'pieces of chicken left over!')
elif more == 1:
    print('Dr. Chaz needs 1 more piece of chicken!')
else:
    print('Dr. Chaz needs',more,'more pieces of chicken!')









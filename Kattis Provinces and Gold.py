



# Provinces and Gold
# https://open.kattis.com/problems/provincesandgold




x,y,z = map(int, input().split(' '))


total = x*3 + y*2 + z

vc = ['Province','Duchy','Estate']
tc = ['Gold','Silver','Copper']

if total > 7:
    print(vc[0],end=' or ')
elif total > 4:
    print(vc[1],end=' or ')
elif total > 1:
    print(vc[2],end=' or ')
if total > 5:
    print(tc[0])
elif total > 2:
    print(tc[1])
else:
    print(tc[2])






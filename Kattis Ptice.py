

# Ptice
# https://open.kattis.com/problems/ptice

adrian = 'ABCABCABCABC'
bruno = 'BABCBABCBABC'
goran = 'CCAABBCCAABB'

items = int(input())
s = input()
at = 0
bt = 0
gt = 0

p = 0
for i in s:
    if i == adrian[p]:
        at+=1
    if i == bruno[p]:
        bt+=1
    if i == goran[p]:
        gt+=1
    p+=1
    if p == 12:
        p = 0


maxi = max(at,bt,gt)
print(maxi)
if at == maxi:
    print('Adrian')
if bt == maxi:
    print('Bruno')
if gt == maxi:
    print('Goran')















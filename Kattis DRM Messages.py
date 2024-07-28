
# DRM Messages
#https://open.kattis.com/problems/drmmessages

s = input()
mid = int(len(s)/2)

s1 = s[:mid]
s2 = s[mid:]

x = 0
y = 0

for i in range(len(s1)):
    x = ord(s1[i])-65+x
    y = ord(s2[i])-65+y

s1n = ""
s2n = ""

x = x%26
y = y%26


for i in range(len(s1)):
    a = ord(s1[i]) + x
    b = ord(s2[i]) + y


    if a > 90:
        a = a-26
    if b > 90:
        b = b-26
    s1n = s1n+chr(a)
    s2n = s2n+chr(b)
# Works to Here

ans = ""

for i in range(len(s2)):
    a = ord(s1n[i])
    b = ord(s2n[i])
    b = b-65
    a = a+b

    if a > 90:
        a = a-26
    ans = ans+chr(a)


print(ans)

#A = 64
# 90 = 90













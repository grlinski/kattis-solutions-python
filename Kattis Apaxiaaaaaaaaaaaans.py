
# Apaxiaaaaaaaaaaaans
# https://open.kattis.com/problems/apaxiaaans


s = input()



ns = s[0]

for i in range(1,len(s)):
    if s[i] == s[i-1]:
        pass
    else:
        ns = ns+s[i]
print(ns)


















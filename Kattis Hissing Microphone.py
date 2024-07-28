


s = input()
ans = "no hiss"
for i in range(0,len(s)-1):
    if s[i] == 's' and s[i+1] == 's':
        ans = 'hiss'
        break
print(ans)















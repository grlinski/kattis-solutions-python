

s = input()

"""

%3
0 = P
1 = E
2 = R


"""
total = 0
for i in range(0,len(s)):
    q = i%3
    if q==0 and s[i] == 'P':
        pass
    elif q == 1 and s[i] == 'E':
        pass
    elif q == 2 and s[i] == 'R':
        pass
    else:
        total+=1
print(total)



















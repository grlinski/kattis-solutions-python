

# Alphabet Spam
# https://open.kattis.com/problems/deathknight


s = input()

# Whitespace
# lower
# upper
# symbols


ws = 0
lo = 0
up = 0
sy = 0


for i in s:
    if i == "_":
        ws+=1
    elif i.islower():
        lo+=1
    elif i.isupper():
        up+=1
    else:
        sy+=1


total = ws+lo+up+sy
print(ws/total)
print(lo/total)
print(up/total)
print(sy/total)



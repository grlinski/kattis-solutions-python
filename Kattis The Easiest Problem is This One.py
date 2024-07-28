
# The Easiest Problem Is This One
# https://open.kattis.com/problems/easiest



def intsum(x):
    s = str(x)
    total = 0
    for i in s:
        total = total+int(i)
    return total



while True:
    s = input()
    if s == '0':
        break

    num = int(s)
    sum = intsum(s)

    multi = 11
    while True:
        y = str(num*multi)
        x = intsum(y)
        if x == sum:
            print(multi)
            break
        multi+=1








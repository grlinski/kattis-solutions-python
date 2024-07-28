

# Stacking Cups
# https://open.kattis.com/problems/cups


items = int(input())
dict = {}
list1 = []
for i in range(items):
    x,y = input().split()

    try:
        a = int(int(x)/2)
        b = y
    except:
        a = int(y)
        b = x

    dict[a] = b
    list1.append(a)


list1.sort()

for i in list1:
    print(dict[i])
















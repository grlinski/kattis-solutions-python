

ans = []
items = int(input())
ender = 0
while ender!=12:
    uni, name = input().split()
    if uni not in ans:
        ans.append(uni)
        print(uni,name)
        ender+=1











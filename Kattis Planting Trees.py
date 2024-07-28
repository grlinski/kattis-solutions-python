

# Planting Trees
# https://open.kattis.com/problems/plantingtrees

times = int(input())

x = list(map(int, input().strip().split(' ')))
leng = len(x)-1
orileng = leng+1

x.sort(reverse=True)
for i in range(0,len(x)):
    x[i] =x[i] - leng
    leng-=1

maxi = max(x)
print(maxi+orileng+1)


"""
1 Day to Plant
Day after last tree has matured, is ans




"""

















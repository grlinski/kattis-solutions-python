

# Sum Kind of Problem
# https://open.kattis.com/problems/sumkindofproblem
# Completed



times = int(input())
for i in range(times):
    k,n = map(int, input().split(' '))
    sumall = 0
    sumodd = 0
    sumeven = 0

    # n is even
    if n%2 == 0:
        sumall = (n+1)*(n//2)
        sumeven = sumall*2
        sumodd=sumeven-n
    else:
        sumodd = n**2
        sumeven = sumodd+n
        sumall = ((n+1)//2)*n

    print(k,sumall,sumodd,sumeven)







"""
6
1 10
2 11
3 12
4 13
5 14
6 15


3
1 10
3 12
5 14


3
2 11
4 13
6 15








"""











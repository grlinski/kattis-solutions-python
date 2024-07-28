

# Sum Kind of Problem
# https://open.kattis.com/problems/sumkindofproblem

# Time Limit Exceeded




times = int(input())
for i in range(times):
    k,n = map(int, input().split(' '))
    sumall = 0
    sumodd = 0
    sumeven = 0
    s1,s2,s3 = n,n,n
    num = 1
    while s1 !=0 or s2!=0 or s3!=0:

        if s1 !=0:
            sumall = sumall+num
            s1-=1
        if s2 !=0 and num%2 != 0:


            sumodd = sumodd+num


            s2-=1
        if s3 !=0 and num%2 == 0:
            sumeven = sumeven+num
            s3-=1
        num+=1
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











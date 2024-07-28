
# Last Factorial Digit
# https://open.kattis.com/problems/lastfactorialdigit

t = int(input())
for i in range(t):
    n = int(input())
    total = 1
    for j in range(1,n+1):
        total=total*j

    print(total%10)
















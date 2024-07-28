


# Skocimis
# https://open.kattis.com/problems/skocimis


a, b, c = map(int, input().split(' '))

# a is always the lowest, then b then c


ans1 = c-b-1
ans2 = b-a-1
print(max(ans1,ans2))




"""

3 5 9



"""



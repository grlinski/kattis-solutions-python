
# Kattis boat Parts
# https://open.kattis.com/problems/boatparts

parts, days = map(int, input().split(' '))

set1 = set()
pa = False

for i in range(days):
    set1.add(input())
    if len(set1) == parts:
        print(i+1)
        pa = True

        break

if pa == False:
    print('paradox avoided')
















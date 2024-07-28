

# Bus
# https://open.kattis.com/problems/bus


cases = int(input())

for i in range(cases):
    stops = int(input())
    people = 0

    for j in range(stops):
        people = (people+0.5)*2

    print(int(people))


























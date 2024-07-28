
# Booking a Room
# https://open.kattis.com/problems/bookingaroom


r,n = map(int, input().split(' '))
rooms = []

for i in range(1,r+1):
    rooms.append(i)

for i in range(n):
    x = int(input())
    if x in rooms:
        rooms.remove(x)

if len(rooms) == 0:
    print('too late')
else:
    print(rooms[0])
















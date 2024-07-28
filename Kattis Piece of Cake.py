
# Piece of Cake
# https://open.kattis.com/problems/pieceofcake2

s,x,y = map(int, input().split(' '))

x2 = s-x
y2 = s-y

s1 = x*y*4
s2 = x2*y*4
s3 = x2*y2*4
s4 = x*y2*4
print(max(s1,s2,s3,s4))


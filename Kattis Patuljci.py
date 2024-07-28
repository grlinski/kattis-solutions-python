

# Patuljci
# https://open.kattis.com/problems/patuljci

q = []
for i in range(0,9):
    x = int(input())
    q.append(x)

total = sum(q)
diff = total-100

a = 0
b = 1

while True:
     x = q[a]
     y = q[b]

     if x+y == diff:
         #print(x,y)
         q.remove(x)
         q.remove(y)

         break
     b+=1
     if b==9:
         a+=1
         b=a+1



for i in q:
    print(i)



















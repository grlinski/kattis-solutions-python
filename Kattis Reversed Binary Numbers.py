
# Reversed Binary Numbers

# https://open.kattis.com/problems/reversebinary



x = int(input())
y = bin(x)
y = y[2:]
y = y[::-1]
x = int(y,2)
print(x)







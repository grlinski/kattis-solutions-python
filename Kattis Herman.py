

# Herman
# https://open.kattis.com/problems/herman
import math

radius = float(input())

print(math.pi*(radius**2))
x = round(((radius**2)*2),10)
x = x+0.00000000001
print(x)












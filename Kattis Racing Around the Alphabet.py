
import math


# Length = 27

circ = math.pi*60
seg = circ/28
ex = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ_\''




def pickup(s):
    total = 1

    for i in range(0,len(s)-1):
        total = total+1
        total = total+short(s[i],s[i+1])

    return total






# Shortest Distance Between two Characters
def short(x,y):



    ix = ex.index(x)
    iy = ex.index(y)

    diff = abs(ix-iy)
    if diff > 14:
        diff = abs(28-diff)

    time = (diff*seg)/15
    return time





times = int(input())


for i in range(times):
    qs = input()
    s = qs.replace(" ","_")

    print(pickup(s))



"""
How 
15 ft/second
circumference = 




1
WINNING ISN'T EVERYTHING IT'S THE ONLY THING


"""






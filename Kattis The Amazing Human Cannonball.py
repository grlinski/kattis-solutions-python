
import math

times = int(input())
for i in range(times):
    v0,angle,x,h1,h2 = map(float, input().split(' '))



    #So at x distance will the person be in the gap?

    # Use values to calculate t
    # Use t to calulate y


    c = math.cos(angle*0.0174533)
    s = math.sin(angle*0.0174533)
    #print(c)
    t = x/(c*v0)
    #print(t)

    y = (v0*t*s) - (0.5*9.81*(t**2))

    if y > h1+1 and y < h2-1:
        print('Safe')
    else:
        print('Not Safe')






"""

1
19 45 20 9 12

"""





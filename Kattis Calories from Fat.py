

# Calories from Fat
# https://open.kattis.com/problems/calories

#fat, pro, sug, star, alcho

# grams, cals, or % of calories



import re

digi = r'\d+'
typer = r'[gC%]'
conv = [9,4,4,4,7]
calories = [0,0,0,0,0]

#x = input()
x = '3g 10g 10% 0g 0g'

d = re.findall(digi, x)
t = re.findall(typer,x)
for i in range(0,len(d)):
    if t[i] == 'C':
        calories[i] = int(d[i])
    elif t[i] == 'g':
        calories[i] = int(d[i])*conv[i]


print(calories)






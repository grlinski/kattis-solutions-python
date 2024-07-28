

# Peragrams

# https://open.kattis.com/problems/peragrams

x = input()


# Basically how many letters do we need to remove for the string to be an anagram of a palindrome

alpha = [0]*26

for i in x:

    pos = ord(i)-97

    alpha[pos]+=1

leng = len(x)
if len(x)%2 == 0:
    oneodd = True
else:
    oneodd = False

remove = 0

for i in range(0,len(alpha)):
    x  = alpha[i]
    if x%2 ==0:
        alpha[i] = x % 2
        pass
    elif x%2 == 1 and oneodd == False:
        alpha[i] = x%2
        oneodd = True
    elif x%2 == 1 and oneodd == True:
        alpha[i] = x % 2
        remove+=1



if remove == leng:
    print(remove-1)
else:
    print(remove)



"""

A palindrome will have an equal amounts of all letters except for possible one in the middle.

So



"""














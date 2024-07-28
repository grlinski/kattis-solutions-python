



# Poker Hand
# https://open.kattis.com/problems/pokerhand

"""
Note, this was quite simple
I only needed to look at the number value of the cards not the suit value
However in my codiing I got suit and number value swapped.

However this program does work now on kattis, but could likely be modifyed to make sense later



"""




suits = {}
val = {}

s = input().split()

for i in s:
    x = i[0]
    y = i[1]
    if y in val:
        val[y]+=1
    else:
        val[y]=1

    if x in suits:
        suits[x]+=1
    else:
        suits[x]=1


maxi1 = max(suits.values())
maxi2 = max(val.values())
print(maxi1)




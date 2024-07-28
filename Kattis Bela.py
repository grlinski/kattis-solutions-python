

# Bela
# https://open.kattis.com/problems/bela


t,dom = input().split()
times= int(t)

times=times*4
total = 0
for i in range(0,times):
    h = input()
    num = h[0]
    suit = h[1]
    if num == 'A':
        total = total+11
    elif num == 'K':
        total = total+4
    elif num == 'Q':
        total = total+3
    elif num == 'T':
        total = total+10
    elif num == '7':
        total = total + 0
    elif num == '8':
        total = total + 0
    elif num == 'J' and suit == dom:
        total = total + 20
    elif num == 'J':
        total = total + 2
    elif num == '9' and suit == dom:
        total = total + 14
    elif num == '9':
        total = total + 0



print(total)


















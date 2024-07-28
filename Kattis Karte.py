

# Karte
# https://open.kattis.com/problems/karte

p = []
k = []
h = []
t = []
cards = []

s = input()

for i in range(0,len(s),3):
    suit = s[i]
    x = s[i+1:i+3]
    num = int(x)

    #print(suit,num)

    on = True

    if suit == "P":
        if num in p:
            print('GRESKA')
            on = False
            break
        else:
            p.append(num)

    elif suit == "K":
        if num in k:
            print('GRESKA')
            on = False
            break
        else:
            k.append(num)

    elif suit == "H":
        if num in h:
            print('GRESKA')
            on = False
            break
        else:
            h.append(num)

    elif suit == "T":
        if num in t:
            print('GRESKA')
            on = False
            break
        else:
            t.append(num)



if on == True:
    print(13-len(p),13-len(k),13-len(h),13-len(t))














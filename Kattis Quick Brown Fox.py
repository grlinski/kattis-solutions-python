
# Quick Brown Fox
# https://open.kattis.com/problems/quickbrownfox

times = int(input())

all = ['a' ,'b' ,'c' ,'d' ,'e' ,'f' ,'g' ,'h' ,'i' ,'j' ,'k' ,'l' ,'m' ,'n' ,'o' ,
       'p' ,'q' ,'r' ,'s' ,'t' ,'u' ,'v' ,'w' ,'x' ,'y' ,'z']


for i in range(times):
    s = input()

    letters = ['a' ,'b' ,'c' ,'d' ,'e' ,'f' ,'g' ,'h' ,'i' ,'j' ,'k' ,'l' ,'m' ,'n' ,'o' ,
       'p' ,'q' ,'r' ,'s' ,'t' ,'u' ,'v' ,'w' ,'x' ,'y' ,'z']

    for j in s:
        k = j.lower()
        if k in letters:
            letters.remove(k)

    if len(letters) == 0:
        print('pangram')
    else:
        print('missing ',end='')
        for e in letters:
            print(e,end='')
    print()











"""

3
abcdefgHijklmnopqrstuvqxyz
abcdefgHijklmnopqrstuvqxy
a a a a a a a 2324634634124 124124 1 * * 3234234



"""




















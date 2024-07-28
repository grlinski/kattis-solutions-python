
# Mastering Mastermind
# https://open.kattis.com/problems/mastermind




def correct(a,g):
    ans = 0
    s1 = ''
    s2 = ''
    for i in range(0,len(a)):
        if a[i] == g[i]:
            ans+=1
        else:
            s1+=a[i]
            s2+=g[i]


    ans2 = ordered(s1,s2)
    return ans,ans2

def ordered(s1,s2):
    dicta = {}
    dictg = {}
    items = set()
    for i in range(0,len(s1)):
        a = s1[i]
        g = s2[i]
        items.add(a)
        items.add(g)
        if a in dicta:
            dicta[a]+=1
        else:
            dicta[a] = 1

        if g in dictg:
            dictg[g]+=1
        else:
            dictg[g] = 1

    ans = 0
    a1 = 0
    g1 = 0
    for i in items:



        if i in dicta:
            a1 = dicta[i]
        else:
            a1 = 0
        if i in dictg:
            g1 = dictg[i]
        else:
            g1 = 0

        ans+=min(a1,g1)

    return ans





x,a,g  = input().split(' ')



ans1,ans2 = (correct(a,g))
print(ans1,ans2)

















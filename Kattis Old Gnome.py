


# Old Gnome
# https://open.kattis.com/problems/oddgnome


times = int(input())

for i in range(times):
    q = list(map(int, input().strip().split(' ')))
    del(q[0])

    for j in range(0,len(q)-1):
        x = q[j]
        y = q[j+1]
        z = q[j-1]




        # Normal
        if y-1 == x:
            #print(x,j)
            pass
        else:
            print(j+2)
            break






# Reverse Rot
# https://open.kattis.com/problems/reverserot


ex = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ_.'
# Length = 27

while True:
    q = input().split()
    t = int(q[0])
    if t == 0:
        break

    s = q[1]
    r = s[::-1]
    ns = ""


    for i in r:
        dex = ex.index(i)
        dex = dex+t

        if dex > 27:
            dex = dex-28
        new = ex[dex]
        ns = ns+new
    print(ns)













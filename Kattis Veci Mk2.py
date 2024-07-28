
def digi_swap(x):


    ori =''
    orinum= 0

    for i in x:
        ori = ori+str(i)

    orinum= int(ori)


    swap = False
    # First Swap
    for i in range(len(x)-1,0,-1):
        right = x[i]
        left = x[i-1]
        # Does First Swap and Stops
        if left < right:
            hold = right
            x[i] = left
            x[i-1] = hold
            swap = True
            start = i-1
            break
    if swap == False:
        return 0
    head = x[:start+1]
    end = x[start+1:]
    end.sort()
    rend = end[::-1]
    ans = head+end
    s = ''
    for i in ans:
        s = s+str(i)


    if int(s) <= orinum:
        return 0

    return s





x = input()
digi = []
for i in x:
    digi.append(int(i))

print(digi_swap(digi))






# Kattis Veci
# https://open.kattis.com/problems/veci


# Fails the last testcase
# No idea why.



def digi_swap(x):

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

    ans = head+end
    s = ''
    for i in ans:
        s = s+str(i)

    if int(s) <= (int(x)):
        return 0

    return s





x = input()
digi = []
for i in x:
    digi.append(int(i))

print(digi_swap(digi))




"""

Process
Digit Swap Two Adjacent Digits, only if the left one is higher than the right one.
Then make sure everything after those two digits, to the right are in acsending order.


"""
















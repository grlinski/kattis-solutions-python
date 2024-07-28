

# Death Knight Hero
# https://open.kattis.com/problems/deathknight


times = int(input())

win = 0
for i in range(times):

    s = input()
    win +=1
    for j in range(0,len(s)-1):
        if s[j] == 'C' and s[j+1] == 'D':
            win -=1
            break


print(win)



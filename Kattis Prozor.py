

# Prozor
# https://open.kattis.com/problems/prozor


def flies(l,r,t,b,q):
     # Y Shows area
    total = 0
    for i in range(t,b):
        for j in range(l,r):
            y = q[i]

            x = q[i][j]
            if x == '*':
                total+=1
        #print(y[l:r])

    return total





q = []
ro,c,k = map(int, input().split(' '))

for i in range(ro):
    u = input()
    q.append(u)


# Actual Racket Size
rckt = k-2


end = False
maxi = 0
prev = 0
tf = 0

# Down, Start at 1 since we can't actually get the top or bottom rows
for i in range(1,ro):
    # Across
    for j in range(1,c):
        l = j
        r = j+rckt
        t = i
        b = i+rckt
        #print(j,i)

        if b >ro:
            end = True
            break

        if r > c:
            break

        new = (flies(l,r,t,b,q))
        num = max(prev,new)
        if num > maxi:
            maxi = num
            # Coordinates of Racket Area
            rl = l-1
            rr = r
            rt = t-1
            rb = b
            #print(num)


    if end == True:
        break



# Mostly Works til Here
# Need to Get Correct Coordinates of the Racket Area


#print('L R T B')
#print(rl,rr,rt,rb)
print(maxi)


# Print/Change Array Q
# Down i
for i in range(0,ro):
    # Across j
    for j in range(0,c):
        # Pluses
        if (i == rt and j == rl) or (i == rt and j == rr) or(i == rb and j == rl) or (i == rb and j == rr):
            print("+", end="")
        # Across Dashes -
        elif (j > rl and j < rr and (i == rb or i == rt)):
            print('-',end='')
        # Down pipes |
        elif (i > rt and i < rb and (j == rr or j == rl)):
            print('|',end='')
        else:
            print(q[i][j],end="")
    print()





    # Continue unitl bottom right of the racket hits the end
    # br == q[r-1][c-1] = end





















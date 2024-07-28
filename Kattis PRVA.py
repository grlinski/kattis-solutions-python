
# Prva
# https://open.kattis.com/problems/prva

# Rows Columns
r,c = map(int, input().split(' '))


q = []
pad = "#"*(c+2)
q.append(pad)
for i in range(r):
    x = input()
    x = "#"+x+'#'

    q.append(x)

q.append(pad)


sword = ''
lword = 10000


# Across
r = r+2
c = c+2
amt = r*c
end = 0

ar = 0
dr = 0
ac = 0
dc = 0

acs = ''
ds = ''
wordlist = []


while True:
    end+=1
    if end == amt+1:
        break


    # Across, col changes, then row
    if q[ar][ac] == '#':
        if len(acs) > 1:
            sword = acs
            wordlist.append(sword)
            lword = len(acs)
            acs = ''
        acs = ''
    else:
        acs = acs + q[ar][ac]

    # Across Changes
    if ac+1 == c:
        ac=0
        ar+=1
    else:
        ac+=1


    # Down, row changes, then col
    if q[dr][dc] == '#':
        if len(ds) > 1:
            sword = ds
            wordlist.append(sword)
            lword = len(ds)
            ds = ''
        ds = ''
    else:
        ds = ds + q[dr][dc]


    if dr+1 == r:
        dr=0
        dc+=1
    else:
        dr+=1








wordlist.sort()
print(wordlist[0])


"""



        # Across Words
        if q[i][j] == '#':
            print(i,j)
            if len(acs) >1 and len(acs)< lword:
                sword = acs
                lword = len(acs)
                acs = ''

            acs = ''
        else:
            acs = acs+q[i][j]
    
    
        # Down Words
    if q[j][i] == '#':
        if len(ds) >1 and len(ds)< lword:
            sword = ds
            lword = len(ds)
            ds = ''
        ds = ''
    else:
        ds = ds+q[j][i]








"""


















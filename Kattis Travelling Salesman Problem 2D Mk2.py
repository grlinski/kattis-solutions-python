

# Travelling Salesperson 2D
# https://open.kattis.com/problems/tsp


# Gets Distances between 2 x,y coordinates
# Doesn't require the Math Module
def distance(x1,y1,x2,y2):
    dis = ((abs(x1-x2)**2)+(abs(y1-y2)**2))**(1/2)
    return dis


# Row Minimization
# All Values in a row are now subtracted by the lowest value in the row
# Had to watch out for None values, obviously points shouldn't have a distance from themselves, ie) zero
def rowmini(matrix):
    for i in range(0, len(matrix)):

        r = matrix[i]
        # mini = min(both)
        #
        mini = min(x for x in r if x is not None)
        # print(mini)
        for j in range(0, len(matrix[i])):
            if matrix[i][j] != None:
                # print(dismatrix[i][j])
                matrix[i][j] = matrix[i][j] - mini
                pass
    return matrix



# Col Minimization
# Basically a flip of row Minimization
# Have to append all items in a col to a list

def colmini(matrix):
    for i in range(0, len(matrix[0])):

        col = []
        for j in range(0, len(matrix[i])):
            if matrix[i][j] != None:
                col.append(matrix[j][i])

        mini = min(col)
        if mini != 0:
            for j in range(0, len(matrix[i])):
                if matrix[i][j] != None:
                    matrix[j][i] = matrix[j][i] - mini
    return matrix



# Penalties of Zero
def penz(x):
    pass





t = int(input())
q = []



for i in range(t):
    x,y = (map(float, input().strip().split(' ')))
    q.append([x,y])



dismatrix = []

for i in q:
    hold = []
    for j in q:
        x1 = i[0]
        y1 = i[1]
        x2 = j[0]
        y2 = j[1]

        if x1 == x2 and y2 == y1:
            hold.append(None)
        else:
            d = distance(x1,y1,x2,y2)
            hold.append(d)
    dismatrix.append(hold)


dismatrix = rowmini(dismatrix)
dismatrix = colmini(dismatrix)




# !!!!!!! NEXT THING TO DO in case I forget
# Work on Penalties of Zero
# https://www.youtube.com/watch?v=vNqE_LDTsa0
# Around 7 min mark



# Penalties of Zeroes
# Store highest penalites
zpen = []







"""
for i in dismatrix:
    print()
    for j in i:
        if j == None:
            print('N',end=" ")
        else:
            print(round(j),end=" ")

"""















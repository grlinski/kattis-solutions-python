

# ToLower
# https://open.kattis.com/problems/tolower



# Takes in list X, converts first letter of each entry to lowercase
# Return new list y
def first_low(x):
    y = []
    for w in x:
        ns = ''
        firstlet = True
        for j in range(len(w)):
            if firstlet == True:
                ns = ns+(w[j].lower())
                firstlet = False
            else:
                ns = ns + (w[j])
        y.append(ns)

    return y


def passes(y):

    for w in y:
        for i in range(len(w)):
            a = w[i]
            
            if a.isupper():
                return False

    return True






p,t = map(int, input().split(' '))

correct = 0

for i in range(t):
    q = []

    for j in range(p):
        x = input()
        q.append(x)

    # List of first letter to lowercase
    y = first_low(q)

    ans = passes(y)

    if ans == True:
        correct+=1

print(correct)

























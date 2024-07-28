

#Kattis CD
# https://open.kattis.com/problems/cd



# Lists Better?
#????

jack,jill = map(int, input().split(' '))

jackset = set()
jillset = set()
all = []
setter = set()
lister = []
total = 0
for i in range(jack):
    x = input()
    setter.add(x)
    lister.append(x)
    jackset.add(x)
for i in range(jill):
    x = input()
    setter.add(x)
    lister.append(x)
    jillset.add(x)


ljill = len(jillset)
ljack = len(jackset)
lset = len(setter)
llist = len(lister)

#print(ljack)
#print(ljill)
#print(lset)
#print(llist)




print(llist-lset)









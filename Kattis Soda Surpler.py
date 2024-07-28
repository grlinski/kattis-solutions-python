

# Soda Surpler
# https://open.kattis.com/problems/sodasurpler





x,y,z, = (map(int, input().strip().split(' ')))



cans = x+y
drank = 0


while True:
    if cans < z:
        break

    newcans = (cans%z) + (cans//z)
    drank = drank+(cans//z)
    cans = newcans


print(drank)




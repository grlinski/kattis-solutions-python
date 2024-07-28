
# Faktor
# https://open.kattis.com/problems/faktor
import math


arts,imp = map(int, input().split(' '))

# bribe = q/arts
# Always round up go for lowest float

# Want lowest amount of cites

#imp = cites/arts
cites = arts*imp

cites-=1
checker = imp
prev = imp
while True:
    checker = cites/arts
    cites-=1
    if math.ceil(checker) == imp-1:
        break
    prev = checker

print(int(prev*arts))
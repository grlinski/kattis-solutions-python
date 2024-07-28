
import sys,os
# Compound Words
# https://open.kattis.com/problems/compoundwords

"""

a bb
ab b


"""
q = []
while True:

    x = input().split()

    if not x:
        break

    y = x[0]
    for i in x:
        q.append(i)









words = []
set1 = set()
word1 = ''
word2 = ''
p1 = 0
p2 = 1

length = len(q)-1

while True:
    word1 = q[p1]
    word2 = q[p2]
    s = word1+word2

    words.append(s)
    set1.add(s)
    print(s)

    p2+=1


    if p2 == p1:
        p2+=1
    if p2 >= length and p1 >= length:
        break
    if p2 == length:
        p2 = 0
        p1+=1
    if p2 >= length and p1 >= length:
        break

words = list(set1)
words.sort()
for i in words:
    print(i)














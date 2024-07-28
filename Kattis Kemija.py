

# Kemija
# https://open.kattis.com/problems/kemija08


vowels = 'aeiou'
def decode(x):
    ns = ""
    p = 0
    end = len(x)
    while True:
        if x[p] in vowels:
            ns = ns+x[p]
            p+=3
        else:
            ns = ns+x[p]
            p+=1
        if p >= end:
            break
    return ns



s = input().split()

for i in s:
    print(decode(i),end=" ")








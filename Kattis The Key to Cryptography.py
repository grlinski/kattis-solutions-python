

# The Key to Cryptography
# https://open.kattis.com/problems/keytocrypto


"""

shift
A = 0
Z = 25

Unicode

A = 65
Z = 90
2


"""


def encode(x,y):
    length = len(x)

    nx = y+x
    ns = ""
    for i in range(length):
        new = ord(x[i])+(ord(nx[i])-65)
        if new > 90:
            new = new-26
        ns = ns+chr(new)

    return ns



def decode(ct,k):
    length = len(ct)

    ns = ""


    for i in range(length):
        move = ord(k[i])-65
        new = ord(ct[i])- move
        if new < 65:
            new = new+26
        k = k+chr(new)
        ns = ns+chr(new)


    return ns


s = input()
e = input()


print(encode(s,e))
print(decode(s,e))










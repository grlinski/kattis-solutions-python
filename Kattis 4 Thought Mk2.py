
# 4 Thought Mk2
# https://open.kattis.com/problems/4thought


# Maybe just easiest to generate every number possible.
"""

This Mk2 just really adds a dictionary to store info




Notes:
Order of operations matter
BEDMAS
No brackets allowed though

So Multi and Div
Then add and sub.
No concatenation, so no 44 or 444s and such
No decimals allowed in any part
So 10/4 = 2
Integer divison only.

Highest Number I can make is 256
Lowest is -256



May need to swap a negative sign into the front


Also I only need to perform a max of 3 operations


"""

import itertools
from itertools import permutations
from itertools import combinations

def add(a ,b):
    return a+ b, '+'


def sub(a, b):
    return a - b, '-'


def mult(a, b):
    return a * b, '*'


def div(a, b):
    return a // b, '/'


def order(m, n, o, dict):
    # Mult and Div First, then add and subtract

    # Need to Seperated into parts
    # Ex , 4*4 + 4*4, Part 1 and Part 3 go first then Part 2

    # If m is div or mult
    if m == div or m == mult:
        p1, op1 = m(4, 4)
        if n == div or n == mult:
            p2, op2 = n(p1, 4)
            ans, op3 = o(p2, 4)
        elif o == div or o == mult:
            p3, op3 = o(4, 4)
            ans, op2 = n(p1, p3)
        else:
            p2, op2 = n(p1, 4)
            ans, op3 = o(p2, 4)
    # If m is not div or mult but n is.
    elif (m == add or m == sub) and (n == mult or n == div):
        p2, op2 = n(4, 4)
        if o == div or o == mult:
            p3, op3 = o(p2, 4)
            ans, op1 = m(4, p3)
        else:
            p1, op1 = m(4, p2)
            ans, op3 = o(p1, 4)
    # If only o is div or mult, only one way to do things.
    elif (o == mult or o == div):
        p3, op3 = o(4, 4)
        p1, op1 = m(4, 4)
        ans, op2 = n(p1, p3)
    # All are either add or sub
    else:
        p1, op1 = m(4, 4)
        p2, op2 = n(p1, 4)
        ans, op3 = o(p2, 4)


    equ = '4 '+str(op1)+ ' 4 '+ str(op2)+ ' 4 ' +str(op3) + ' 4 '+ '= '+ str(ans)
    #equneg = '-4 '+str(op1)+ ' 4 '+ str(op2)+ ' 4 ' +str(op3) + ' 4 '+ '= '+ str(ans)
    dict[ans] = equ
    #dict[-ans] = equneg
    return dict

    #print('4', op1, '4', op2, '4', op3, '4', '=', ans)



dict = {}
# operations = (add,sub,mult,div)
operations4 = (add, add, add, add, sub, sub, sub, sub, mult, mult, mult, mult, div, div, div, div)

x = (list(itertools.permutations(operations4, 3)))
for i in x:
    order(i[0], i[1], i[2],dict)

t = int(input())
for i in range(t):
    y = int(input())
    if y in dict:
        print(dict[y])
    else:
        print('no solution')




































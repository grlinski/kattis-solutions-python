

# Prime Path
# https://open.kattis.com/problems/primepath

# Learn about nodes and paths.




import math,re
import time

# If I need to save time, just take the prime generation into a list.



# Generates Primes between Start and Stop values inclusively
# Note that 2,3 and 5 should be added manually if they are in range.

def prime_number_genSE(start,end):

    # For whatever reason this doesn't work unless start is 2 or greater
    # So may as well make start 2 as a minimum.
    if start < 2:
        start =2


    list_of_primes = []
    # 2 and 3 added since they are a pain in the ass


    prime = True
    # Main Loop for Prime Gen
    # Goes until our counter of primes hits items

    number = start

    # Manually Add Annoying Numbers
    if number < 3:
        list_of_primes.append(2)
    if number < 4:
        list_of_primes.append(3)
    if number < 6:
        list_of_primes.append(5)

    while number != end:

        prime = True
        # Quick check if prime
        # The number has to be either 6n+1 or 6n-1,
        # Note I had a problem before with using or instead of and.
        # It only needs to be one or the other, not nessicarily both.
        if (number+1)%6 != 0 and (number-1)%6 != 0:
            prime = False

        elif number % 2 == 0 or number % 3 == 0 or number % 5 == 0:
            prime = False
            # If all those fail check if it is divisible by any of the primes in the list
        else:
            # If the potential divisor is greater than the square root of the number it ends
            # This is one of the most important parts
            # Makes it much more efficient
            upto = int(math.sqrt(number))
            for i in range(2, number):
                if i > upto:
                    break
                if number%i == 0:
                    prime = False
                    break



        if prime == True:
            list_of_primes.append(number)

        number+=1


    return list_of_primes



# Note this function is far slower than the above one.
# I'll keep this around for now though
def primeGen():
    primes = []

    for i in range(10,10000):
        prime = True
        if i%2 == 0:
            prime = False
        elif i%3 ==0 or i%5 == 0:
            prime = False
        else:
            x = math.sqrt(i)
            y = x**2
            if x==y:
                prime = False
            else:
                prime = True
                for j in range(2,i):
                    if i%j == 0:
                        prime = False
                        break
        if prime == True:
            primes.append(i)
    return primes




def consensus(a,b,primes):
    if a==b:
        return 0

    # Check if the numbers are even in primes:
    if a not in primes:
        return 'impossible'
    if b not in primes:
        return 'impossible'



    consen = 0


    cur = str(a)
    end = str(b)
    lv = ''
    for i in range(0,len(cur)):
        if cur[i] == end[i]:
            lv+='A'
            consen+=1
        else:
            lv+='X'


    print(lv)
    return consen




def onedegreediff(x):
    lv = 'AAAA'
    # Where A is locked and X is open.
    # Lock value




primes = prime_number_genSE(1000,9999)
print(primes)
print(len(primes))



# Maybe incorporate this into the prime number generation.
def nodes(list1):
    dict = {}
    s1 = time.time()
    for i in range(0,len(list1)):
        for j in range(i+1,len(list1)):
            x = list1[i]
            y = list1[j]


            if list1[i] not in dict:
                dict[list1[i]] = set()
            if list1[j] not in dict:
                dict[list1[j]] = set()

            xs = str(list1[i])
            ys = str(list1[j])
            if xs[0] != ys[0] and xs[1] == ys[1] and xs[2] == ys[2] and xs[3] == ys[3]:
                dict[x].add(y)
                dict[y].add(x)
            elif xs[0] == ys[0] and xs[1] != ys[1] and xs[2] == ys[2] and xs[3] == ys[3]:
                dict[x].add(y)
                dict[y].add(x)
            elif xs[0] == ys[0] and xs[1] == ys[1] and xs[2] != ys[2] and xs[3] == ys[3]:
                dict[x].add(y)
                dict[y].add(x)
            elif xs[0] == ys[0] and xs[1] == ys[1] and xs[2] == ys[2] and xs[3] != ys[3]:
                dict[x].add(y)
                dict[y].add(x)



    s2 = time.time()
    print(s2-s1)
    print(dict[1097])
    print(dict[8377])
    return dict


# Same thing as above but as a list
# Maybe incorporate this into the prime number generation.
def nodesList(list1):
    dict = {}
    s1 = time.time()
    for i in range(0,len(list1)):
        for j in range(i+1,len(list1)):
            x = list1[i]
            y = list1[j]


            if list1[i] not in dict:
                dict[list1[i]] = []
            if list1[j] not in dict:
                dict[list1[j]] = []

            xs = str(list1[i])
            ys = str(list1[j])
            if x in dict[y] or y in dict[x]:
                pass
            elif xs[0] != ys[0] and xs[1] == ys[1] and xs[2] == ys[2] and xs[3] == ys[3]:
                dict[x].append(y)
                dict[y].append(x)
            elif xs[0] == ys[0] and xs[1] != ys[1] and xs[2] == ys[2] and xs[3] == ys[3]:
                dict[x].append(y)
                dict[y].append(x)
            elif xs[0] == ys[0] and xs[1] == ys[1] and xs[2] != ys[2] and xs[3] == ys[3]:
                dict[x].append(y)
                dict[y].append(x)
            elif xs[0] == ys[0] and xs[1] == ys[1] and xs[2] == ys[2] and xs[3] != ys[3]:
                dict[x].append(y)
                dict[y].append(x)



    s2 = time.time()
    print(s2-s1)
    print(dict[1097])
    print(dict[8377])
    return dict



# Decent Pathfinder, However doesn't return the shortest path.
def find_path(graph, start, end,path=[]):
    path = path + [start]
    if start == end:
        return path
    if start not in graph:
        return None
    for node in graph[start]:
        if node not in path:
            newpath = find_path(graph, node, end, path)
            if newpath: return newpath
    return None

# Hopefully this will find the shortest path.
def find_shortest_path(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    if start not in graph:
        return None
    shortest = None
    for node in graph[start]:
        if node not in path:
            newpath = find_shortest_path(graph, node, end, path)
            if newpath:
                if not shortest or len(newpath) < len(shortest):
                    shortest = newpath
    return shortest


dict = nodesList(primes)
ans = find_path(dict,1033,8179)
print(ans)
print('----')
for i in dict:
    print(i,dict[i])

s1 = time.time()
ans = find_shortest_path(dict,1033,8179)
s2 = time.time()
print(s2-s1)
print(ans)

print('end')

#a,b = map(int, input().split(' '))
















# Detailed Differences
# https://open.kattis.com/problems/detaileddifferences


times = int(input())


for i in range(times):
    x = input()
    y = input()
    print(x)
    print(y)
    for i in range(len(x)):
        if x[i] == y[i]:
            print('.',end="")
        else:
            print("*",end="")
    print()





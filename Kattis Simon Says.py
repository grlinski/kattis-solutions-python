


# Simon Says
# https://open.kattis.com/problems/simonsays

times = int(input())


for i in range(times):
    s = input()
    simon = s[0:10]
    if simon == 'simon says':
        print(s[11:])






# Speed Limit
# https://open.kattis.com/problems/speedlimit



while True:
    entries = int(input())
    if entries == -1:
        break
    tmiles = 0
    phours = 0
    for i in range(entries):
        miles, hours = map(int, input().split(' '))
        elapsedtime = hours-phours
        tmiles = tmiles+elapsedtime*miles
        phours = hours
    print(tmiles,"miles")


















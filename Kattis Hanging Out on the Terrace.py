

# Hanging out on the Terrace

# https://open.kattis.com/problems/hangingout



limit,events = (map(int, input().strip().split(' ')))

total = 0
denials = 0

for i in range(events):
    m, n = input().split()
    num = int(n)
    if m == "leave":
        total = total-num
    elif m == 'enter':
        if total + num > limit:
            denials+=1
        elif total + num <= limit:
            total = total+num
print(denials)



















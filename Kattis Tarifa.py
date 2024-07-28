

# Tarifa
# https://open.kattis.com/problems/tarifa



data = int(input())
months = int(input())
total = data
for i in range(0,months):
    used = int(input())
    total = total+data-used

print(total)




















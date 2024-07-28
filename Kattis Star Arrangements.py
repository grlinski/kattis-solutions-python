

# Star Arrangements
# https://open.kattis.com/problems/stararrangements


# Likely Problems with low Star amounts
# Try 0,1,2,3,4,5


#stars = int(input())
stars = 50
first = 0
second = 0


print(str(stars)+':')
if stars == 3:
    print("2,1")
else:
    for i in range(2,stars-1):
        first = i
        second =i-1
        added = first+second

        # Case 2, first and second are different
        if stars % (added) == 0 or stars % (added) - first == 0:
            print(str(first) + "," + str(second))
        # Case 1, first and second are equal, even and odd amount of rows
        if stars %(first*2) == 0 or stars%(first*2)-first == 0:
            print(str(first) +","+ str(first))


























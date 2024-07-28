


# A New Alphabet
# https://open.kattis.com/problems/anewalphabet


na=['@','8','(','|)','3','#','6','[-]','|','_|','|<','1','[]\/[]','[]\[]','0','|D','(,)','|Z','$',
    '\'][\'', '|_|','\\/','\\/\\/', '}{','`/','2']



# \','\\_\\','\\/','\/\/','}{',''/','2']


x = input()
y = x.upper()

s = ""

for i in y:
    if i.isalpha():
        q = ord(i) -65
        s = s+na[q]
    else:
        s = s+i

print(s)












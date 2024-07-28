

# False Sense of Security
# https://open.kattis.com/problems/falsesecurity


morse={'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
       'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
       'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
       'Y': '-.--', 'Z': '--..', '_': '..--', ',':'.-.-', '.':'---.','?':'----'}

demorse = {'.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F', '--.': 'G', '....': 'H',
        '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P',
           '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T', '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X',
           '-.--': 'Y', '--..': 'Z', '..--': '_', '.-.-': ',', '---.': '.', '----': '?'}


# Converts to Morse Code Without Spaces
# Also Returns a string number of how long each morse code segment is.
def to_morse(x):
    s = ""
    n = ''
    for i in x:

        y = morse[i]
        z = len(y)
        n = n+str(z)
        s = s+y

    return s,n

# Decodes a Morse String Without Breaks
# Returns a string of characters
def decode_morse(morsec,num):

    st = 0
    s = ''
    for i in num:
        ender = int(i)+st
        #print(st,ender)
        n = morsec[st:ender]
        s = s+demorse[n]

        st = ender

    print(s)


q = []
while True:
    try:
        x = input()
        q.append(x)
    except:
        break


for x in q:

    num = ''

    morsea,num = to_morse(x)
    #rmorse = morse[::-1]
    rnum = num[::-1]

    #print(morse)
    #print(num)
    #print(rmorse)
    #print(rnum)

    decode_morse(morsea,rnum)
















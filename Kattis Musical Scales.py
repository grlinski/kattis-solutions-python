


# Musical Scales

# https://open.kattis.com/problems/musicalscales


notes = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#','A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']

pattern = [0,2,4,5,7,9,11,12]

A = ['A' ,'B' ,'C#', 'D', 'E' ,'F#', 'G#']#
As = ['A#', 'C' ,'D', 'D#', 'F' ,'G', 'A']#
B = ['B', 'C#' ,'D#' ,'E' ,'F#', 'G#' ,'A#']#
C = ['C' ,'D' ,'E', 'F', 'G', 'A' ,'B']#
Cs = ['C#', 'D#' ,'F', 'F#', 'G#', 'A#', 'C']#
D = ['D' ,'E', 'F#' ,'G' ,'A' ,'B' ,'C#']#
Ds = ['D#', 'F' ,'G' ,'G#', 'A#', 'C' ,'D']#
E = ['E','F#','G#','A','B','C#','D#']
F = ['F' ,'G', 'A', 'A#', 'C', 'D', 'E']
Fs = ['F#', 'G#' ,'A#', 'B', 'C#' ,'D#', 'F']
G = ['G', 'A' ,'B', 'C', 'D', 'E', 'F#']
Gs = ['G#' ,'A#', 'C', 'C#', 'D#', 'F', 'G']

scales = [A,As,B,C,Cs,D,Ds,E,F,Fs,G,Gs]

# x = Current Note
# Y = Scale to look at
def inscale(x,y):
    if x not in y:
        scales.remove(y)
        #print('rem',y)





t = int(input())
q = input().split()
ender = q[-1]
q.append(ender)
ans = []

for i in q:
    for j in scales:
        inscale(i,j)




if len(scales) == 0:
    print('none')
else:
    for i in scales:
        print(i[0],end= ' ')








# Scale Maker
"""
for i in range(len(notes)):
    for j in (pattern):
        if i+j >= len(notes):
            break
        print('\''  +notes[i+j]+'\'' ,end=' ')

    print()
"""




# Scale
#2,2,1,2,2,2,1









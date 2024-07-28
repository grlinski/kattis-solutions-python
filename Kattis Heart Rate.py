

# Heart Rate
# https://open.kattis.com/problems/heartrate



times = int(input())
for i in range(times):
    bs, ps = input().split()
    b = float(bs)
    p = float(ps)


    # b = beats
    # p = seconds
    bpm = b*60/p


    tbpm = bpm+(60/p)
    bbpm = bpm-(60/p)

    print(bbpm,bpm,tbpm)


























# Sok
# https://open.kattis.com/problems/sok



o,a,p = map(int, input().split(' '))
ro,ra,rp = map(int, input().split(' '))



do = o/ro
da = a/ra
dp = p/rp

ao = 0
aa = 0
ap = 0


if do <= da and do <= dp:
    ao = 0
    aa = a - (do*ra)
    ap = p - (do*rp)

elif da <= do and da <= dp:
    aa = 0
    ao = o - (da*ro)
    ap = p - (da*rp)

elif dp <= da and dp <= do:
    ap = 0
    aa = a - (dp*ra)
    ao = o - (dp*ro)


print(round(ao,4),round(aa,4),round(ap,4))
















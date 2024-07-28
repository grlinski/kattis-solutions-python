

# Paul Eigon
# https://open.kattis.com/problems/pauleigon


n,p,q = map(int, input().split(' '))


ts = p+q
div = ts//5
if ts < n:
    print('paul')


elif div%2 == 0:
    print('paul')
else:
    print('opponent')












# Beavergnaw
# https://open.kattis.com/problems/beavergnaw



import math

pi = math.pi
d,e = (map(int, input().strip().split(' ')))

# Cylinder

# Radius of d
rd = d/2

# Cylinder Volume
vc = pi*(rd**2)*d


# Fustrum volume


Rb = e/2


h = (e-d)/2
vf = (pi*h/3)*((Rb**2)+(Rb*rd) + (rd**2))





# Cylinder Volume
# V = pi*r*r*h

# Frustum Volume
# V = Pi/3 * h(R2 + r2 + R*r)
# http://www.analyzemath.com/Geometry_calculators/surface_volume_frustum.html

tv = r**2*pi*d
fv =









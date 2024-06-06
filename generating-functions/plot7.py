from latextool_basic import *
from latexcircuit import *
from math import sqrt
p = Plot()
p += Grid(x0=-3, x1=3, y0=-3, y1=3)
axes(p=p, x0=-3, x1=3, y0=-3, y1=3)

#X = POINT(x=4, y=0, r=0, label='$\R$ (real axis)', anchor='west')
#p += str(X)
#X = POINT(x=-0.3, y=4.3, r=0, label='$i\R$ (complex axis)',
#          anchor='west')
#p += str(X)

a,b = 0.5, sqrt(3)/2
X = POINT(x=a, y=b, label='$z = 1/2 + i\sqrt{3}/2$',
          anchor='south west')
p += str(X)

a,b = -1,0
X = POINT(x=a, y=b, label='$-1$',
          anchor='south east')
p += str(X)

a,b = 0.5, -sqrt(3)/2
X = POINT(x=a, y=b, label="$z' = 1/2 - i\sqrt{3}/2$",
          anchor='north west')
p += str(X)

#p += Line(points=[(0,b), (a, b)], linestyle='dashed')
#p += Line(points=[(a,0), (a, b)], linestyle='dashed')

p += Circle(x=0, y=0, r=1, linestyle='dashed')
print(p)

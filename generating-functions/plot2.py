from latextool_basic import *
from latexcircuit import *
p = Plot()
p += Grid(x0=-1, x1=4, y0=-1, y1=4)
axes(p=p, x0=-1, x1=4, y0=-1, y1=4)

#X = POINT(x=4, y=0, r=0, label='$\R$ (real axis)', anchor='west')
#p += str(X)
#X = POINT(x=-0.3, y=4.3, r=0, label='$i\R$ (complex axis)',
#          anchor='west')
#p += str(X)

X = POINT(x=3.142, y=0, label='3.14159...',
          anchor='south')
p += str(X)

print(p)

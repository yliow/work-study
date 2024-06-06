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

a,b = 1.5, 1.75
X = POINT(x=a, y=b, label='$a + bi$',
          anchor='south west')
p += str(X)

X = POINT(x=a, y=0, r=0, label='$a$',
          anchor='north')
p += str(X)
X = POINT(x=0, y=b, r=0, label='$b$',
          anchor='east')
p += str(X)


p += Line(points=[(0,b), (a, b)], linestyle='dashed')
p += Line(points=[(a,0), (a, b)], linestyle='dashed')

print(p)

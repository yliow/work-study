from latextool_basic import *
from latexcircuit import *
from math import sqrt
p = Plot()
#p += Grid(x0=-3, x1=3, y0=-3, y1=3)
axes(p=p, x0=-1, x1=3, y0=-1, y1=3)

#X = POINT(x=4, y=0, r=0, label='$\R$ (real axis)', anchor='west')
#p += str(X)
#X = POINT(x=-0.3, y=4.3, r=0, label='$i\R$ (complex axis)',
#          anchor='west')
#p += str(X)

scale = 2
a,b = scale * 0.5, scale * sqrt(3)/2
#X = POINT(x=a, y=b,
#          label=r'{$z = 1/2 + i\sqrt{3}/2$}',
#          anchor='south west')
#p += str(X)

X = POINT(x=a, y=b, label=r"$z = a + bi$", anchor='south west')
p += str(X)

aline = Line(points=[(0,0), (a, b)], linewidth=0.05)
p += aline
x,y = aline.midpoint()
X = POINT(x=x, y=y, r=0, label=r"${r}$", anchor='south east')
p += str(X)

p += Line(points=[(0,0), (a, 0)],  linewidth=0.05)
X = POINT(x=a/2, y=0, r=0, label=r"$a$", anchor='north')
p += str(X)


p += Line(points=[(a,0), (a, b)],  linewidth=0.05)
X = POINT(x=a, y=b/2, r=0, label=r"$b$",
          anchor='west')
p += str(X)

p += arc(x=0.4, y=0, r=0.4, angle0=0, angle1=60)
X = POINT(x=0.5, y=0, r=0, label=r"{$t$}",
          anchor='south')
p += str(X)

print(p)

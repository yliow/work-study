from latextool_basic import *
from latexcircuit import *
from math import sqrt
p = Plot()
#p += Grid(x0=-4, x1=2, y0=-3, y1=3)
axes(p=p, x0=-4, x1=2, y0=-1, y1=3)

#X = POINT(x=4, y=0, r=0, label='$\R$ (real axis)', anchor='west')
#p += str(X)
#X = POINT(x=-0.3, y=4.3, r=0, label='$i\R$ (complex axis)',
#          anchor='west')
#p += str(X)

scale = 3.0
a,b = scale * -0.5, scale * sqrt(3)/2
X = POINT(x=a, y=b,
          label=r'\footnotesize{$z_1 = (-1+\sqrt{3})/2$}',
          anchor='south east')
p += str(X)

#aline = Line(points=[(0,0), (a, b)], linewidth=0.05)
#p += aline
#x,y = aline.midpoint()

# arc
points = []
r = 0.5
for t in list(range(120, 181)):
    t = t * 3.14159265 / 180
    x, y = r * cos(t), r * sin(t)
    x, y = round(x,4), round(y,4)
    points.append((x,y))

p += Line(points=points)

X = POINT(x=-0.7, y=0, r=0, label=r"{$s$}",
          anchor='south')
p += str(X)

p += Line(points=[(a,b), (a,0), (0,0), (a, b)], linewidth=0.05)

X = POINT(x=a/2, y=0, r=0, label=r"\footnotesize{1/2}", anchor='north')
p += str(X)

X = POINT(x=a, y=b/2, r=0, label=r"\footnotesize{$\sqrt{3}/2$}",
          anchor='east')
p += str(X)

print(p)

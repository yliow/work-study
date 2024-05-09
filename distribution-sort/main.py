from latextool_basic import *
from latexcircuit import *
p = Plot()
r = Rect(x0=0, y0=0, x1=5, y1=0.8)
p += r

x,y = r.right()
p += Line(points=[(x+2,y), (x+0.2,y)], endstyle='>', linewidth=0.1)

x,y = r.left()
p += Line(points=[(x-0.2,y), (x - 2,y)], endstyle='>', linewidth=0.1)

x,y = r.bottomleft()
X = POINT(x=x, y=y, r=0, label='head', anchor='north west')
p += str(X)

x,y = r.bottomright()
X = POINT(x=x, y=y, r=0, label='tail', anchor='north east')
p += str(X)

print(p)


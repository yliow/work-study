from latextool_basic import *
from latexcircuit import *
p = Plot()
rect = Rect(x0=0, y0=0, x1=5, y1=5)
p += rect
p += Rect(x0=0-0.4,x1=0-0.4,y0=4.5,y1=4.7,linewidth=0,label=r'$A$')
for i,(x,y) in enumerate([(1,1),(4.5,4),(1,4),(2,3),(2.5, 1.5)]):
    if i != 4: continue
    p += Rect(x0=x-0.1,x1=x+0.1,y0=y-0.1,y1=y+0.1,background='black')
    p += Rect(x0=x-0.4,x1=x-0.4,y0=y,y1=y,
              linewidth=0,label=r'$p_{%s}$' % i)

p += Line(points=[rect.left(), rect.right()])
p += Line(points=[rect.top(), rect.bottom()])

x0,y0 = (-3,-4)
rect0 = Rect(x0=x0,x1=x0+2.5,y0=y0,y1=y0+2.5)
p += rect0
for i,(x,y) in enumerate([(1,4),(2,3)]):
    x = x + x0
    y = y + y0 - 2.5
    p += Rect(x0=x-0.1,x1=x+0.1,y0=y-0.1,y1=y+0.1,background='black')
    p += Rect(x0=x-0.4,x1=x-0.4,y0=y,y1=y,
              linewidth=0,label=r'$p_{%s}$' % (i + 2))

x0,y0 = (x0+3,y0)
rect1 = Rect(x0=x0,x1=x0+2.5,y0=y0,y1=y0+2.5)
p += rect1
for i,(x,y) in enumerate([(4.5,4)]):
    x = x + x0 - 2.5
    y = y + y0 - 2.5
    p += Rect(x0=x-0.1,x1=x+0.1,y0=y-0.1,y1=y+0.1,background='black')
    p += Rect(x0=x-0.4,x1=x-0.4,y0=y,y1=y,
              linewidth=0,label=r'$p_{%s}$' % (i+1))

x0,y0 = (x0+3,y0)
rect2 = Rect(x0=x0,x1=x0+2.5,y0=y0,y1=y0+2.5)
p += rect2

x0,y0 = (x0+3,y0)
rect3 = Rect(x0=x0,x1=x0+2.5,y0=y0,y1=y0+2.5)
p += rect3
for i,(x,y) in enumerate([(1,1)]):
    x = x + x0
    y = y + y0 - 0.5
    p += Rect(x0=x-0.1,x1=x+0.1,y0=y-0.1,y1=y+0.1,background='black')
    p += Rect(x0=x-0.4,x1=x-0.4,y0=y,y1=y,
              linewidth=0,label=r'$p_{%s}$' % i)

p0,p1 = shorten(rect.bottom(), rect0.top(), 0.9)
p += Line(points=[p0,p1])
p0,p1 = shorten(rect.bottom(), rect1.top(), 0.9)
p += Line(points=[p0,p1])
p0,p1 = shorten(rect.bottom(), rect2.top(), 0.9)
p += Line(points=[p0,p1])
p0,p1 = shorten(rect.bottom(), rect3.top(), 0.9)
p += Line(points=[p0,p1])

print(p)

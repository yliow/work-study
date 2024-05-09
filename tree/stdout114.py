from latextool_basic import *
from latexcircuit import *
p = Plot()
rect = Rect(x0=0, y0=0, x1=5, y1=5)
p += rect
p += Rect(x0=0-0.4,x1=0-0.4,y0=4.5,y1=4.7,linewidth=0,label=r'$A$')
for i,(x,y) in enumerate([(1,1),(4.5,4),(1,4),(2,3),(2.5, 1.5)]):
    p += Rect(x0=x-0.1,x1=x+0.1,y0=y-0.1,y1=y+0.1,background='black')
    p += Rect(x0=x-0.4,x1=x-0.4,y0=y,y1=y,
              linewidth=0,label=r'$p_{%s}$' % i)

p += Line(points=[rect.left(), rect.right()])
p += Line(points=[rect.top(), rect.bottom()])

print(p)

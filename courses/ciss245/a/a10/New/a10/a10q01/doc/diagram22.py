from latextool_basic import *
from latexcircuit import *
from intdynarr import *

p = Plot()
obj1 = intdynarr(p, x=1, y=1,
                 members=[('x',''),
                          ('size','6'), ('capacity','12')], label='a')

x,y = obj1['a'].bottomleft()
y -= 0.6
obj2 = Rect(x0=x,y0=y,x1=x+0.4,y1=y+0.4)


x,y = obj2.bottom()
x = 10
c = heaparray(x, y, xs='01234???????')
p += c

p += Line(points=[obj1['x'].center(), c.topleft()], endstyle='>', linewidth=0.02)

print(p)

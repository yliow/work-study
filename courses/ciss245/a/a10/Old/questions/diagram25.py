from latextool_basic import *
from latexcircuit import *
from intdynarr import *

p = Plot()
obj1 = intdynarr(p, x=1, y=1,
                 members=[('x',''),
                          ('size','5'),
                          ('capacity','12')],
                 label='a')
# heap array
r0 = obj1['x']
x,y = r0.bottom()
x = 10
c = heaparray(x, y, xs=[i for i in range(12)])
p += c
# pointer line
p += Line(points=[r0.center(), c.left()], endstyle='>', linewidth=0.02)


print(p)

from latextool_basic import *
from latexcircuit import *
from intdynarr import *

p = Plot()
obj1 = intdynarr(p, x=1, y=1, members=[('x',''), ('size',''), ('capacity','')], label='a')
# heap array
r0 = obj1['x']
x,y = r0.bottom()
x = 10
c = heaparray(x, y, xs='????')
p += c
# pointer line
p += Line(points=[r0.center(), c.left()], endstyle='>', linewidth=0.02)

_,y = obj1['a'].bottom()
y -= 1

#obj2 = intdynarr(p, x=1, y=y, members=[('x',''), ('size',''), ('capacity','')], label='b')
# heap array
#r0 = obj2['x']
#x,y = r0.bottom()
#x = 10
#c = heaparray(x, y, xs='1325')
#p += c
# pointer line
#p += Line(points=[r0.center(), c.left()], endstyle='>', linewidth=0.02)

x,y = obj1['a'].bottomleft()
y -= 0.6
p += str(POINT(x=x, y=y, r=0,
               label=r'\texttt{%s}' % 'b',
               anchor='east'))
p += str(POINT(x=x, y=y, r=0,
               label=r'\texttt{%s}' % '= reference to a',
               anchor='west'))

print(p)

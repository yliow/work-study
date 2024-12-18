from latextool_basic import *
from latexcircuit import *
from intdynarr import *

p = Plot()
obj = intdynarr(p, members=[('x',''), ('size',''), ('capacity','')], label='b')

# heap array
r0 = obj['x']
x,y = r0.bottom()
x = 10
c = heaparray(x, y, xs='632')
p += c
# pointer line
p += Line(points=[r0.center(), c.left()],
          endstyle='>', linewidth=0.02)
    
print(p)

from latextool_basic import *
from latexcircuit import *
from intdynarr import *

p = Plot()
obj1 = intdynarr(p, x=1, y=1,
                 members=[('x',''), ('size',''), ('capacity','')],
                 label='a', do_not_draw=True)
# heap array
r0 = obj1['x']
x,y = r0.bottom()
x = 10
c = Rect(x0=x, y0=y, x1=x+0.5, y1=y+0.5,
         label=r'{\small memory not allocated!}',
         linewidth=0)
p += c

#X = POINT(x=x, y=y, r=0, label='$abcde$', anchor='flushtopleft')
#p += str(X)

# pointer line
#p += Line(points=[r0.center(), c.left()], endstyle='>', linewidth=0.02)

_,y = obj1['a'].bottom()
y -= 1

obj2 = intdynarr(p, x=1, y=y, members=[('x',''), ('size',''), ('capacity','')], label='b')
# heap array
r0 = obj2['x']
p += Line(points=[r0.center(), c.bottomleft()], endstyle='>', linewidth=0.02)

print(p)

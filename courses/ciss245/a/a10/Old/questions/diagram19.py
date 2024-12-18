from latextool_basic import *
from latexcircuit import *
from intdynarr import *

p = Plot()
obj1 = intdynarr(p, x=1, y=1,
                 members=[('x',''),
                          ('size','5'), ('capacity','12')], label='a')
# heap array
r0 = obj1['x']
x,y = r0.bottom()
x = 10
#c = heaparray(x, y, xs='01234')
#p += c

c = Rect(x0=x, y0=y, x1=x+3, y1=y+0.5,
         label=r'{\scriptsize memory not allocated}', linewidth=0)
p += c
# pointer line
p += Line(points=[r0.center(), c.left()], endstyle='>', linewidth=0.02)

# pointer line
p += Line(points=[r0.center(), c.left()], endstyle='>', linewidth=0.02)

x,y = obj1['a'].bottomleft()
y -= 0.6
obj2 = Rect(x0=x,y0=y,x1=x+0.4,y1=y+0.4)
p += obj2

x,y = obj2.left()
p += str(POINT(x=x, y=y, r=0, label=r'\texttt{p}', anchor='east'))

x,y = obj2.bottom()
x = 10
c = heaparray(x, y, xs='01234???????')
p += c
# pointer line
p += Line(points=[obj2.center(), c.left()], endstyle='>', linewidth=0.02)
    
print(p)

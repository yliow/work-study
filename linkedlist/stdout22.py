from latextool_basic import *

def node(x, y, s):
    c = RectContainer(x=x, y=y)
    c += Rect2(x0=0, y0=0, x1=0.7, y1=0.7, label=r'{\texttt{%s}}' % s)
    c += Rect2(x0=0, y0=0, x1=0.7, y1=0.7, label=r'{\texttt{%s}}' % '')
    return c


p = Plot()
n2 = node(0, 0, 2)
n6 = node(0, -2, 6)
n4 = node(2, -2, 4)
n5 = node(3, 0, 5)
p += n2
p += n6
p += n4
p += n5

p += Line(points=[n2[1].center(), n6[0].top()], endstyle='>')
p += Line(points=[n6[1].center(), n4[0].left()], endstyle='>')
p += Line(points=[n4[1].center(), n5[0].bottom()], endstyle='>')

p += Line(points=[(n5[1].topleft()), (n5[1].bottomright())])
p += Line(points=[(n5[1].topright()), (n5[1].bottomleft())])

x,y = n2.bottomleft(); x -= 3
q = Rect2(x0=x, y0=y, x1=x+0.7, y1=y+0.7, label=r'{\texttt{%s}}' % '')
p += q

p += Line(points=[q.center(), n2.left()], endstyle='>')

x,y = q.left(); x -=0.7
p += Rect2(x0=x, y0=y, x1=x, y1=y, label=r'{\texttt{%s}}' % 'phead', linecolor='white')

print(p)

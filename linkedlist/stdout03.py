from latextool_basic import *

def node(x, y, s):
    c = RectContainer(x=x, y=y)
    c += Rect2(x0=0, y0=0, x1=0.7, y1=0.7, label=r'{\texttt{%s}}' % s)
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

p += Line(points=[n2[0].bottom(), n6[0].top()], endstyle='>')
p += Line(points=[n6[0].right(), n4[0].left()], endstyle='>')
p += Line(points=[n4[0].top(), n5[0].bottom()], endstyle='>')

print(p)

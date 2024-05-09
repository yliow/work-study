from latextool_basic import *

def node(x, y, s):
    c = RectContainer(x=x, y=y)
    c += Rect2(x0=0, y0=0, x1=1.5, y1=0.7, label=r'{\texttt{%s}}' % s)
    return c

p = Plot()
n2 = node(0, 0, '(0,4)')
n6 = node(3, 0, '(5,2)')
n4 = node(6, 0, '(9,1)')
n5 = node(9, 0, '(10,6)')
n9 = node(12, 0, '(16,5)')

p += n2
p += n6
p += n4
p += n5
p += n9

p += Line(points=[n2[0].right(), n6[0].left()], endstyle='>', startstyle='>')
p += Line(points=[n6[0].right(), n4[0].left()], endstyle='>', startstyle='>')
p += Line(points=[n4[0].right(), n5[0].left()], endstyle='>', startstyle='>')
p += Line(points=[n5[0].right(), n9[0].left()], endstyle='>', startstyle='>')

print(p)

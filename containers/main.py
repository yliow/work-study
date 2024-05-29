from latextool_basic import *
p = Plot()
c = RectContainer(x=0, y=0)
for i,x in enumerate('126453'):
    if i == 0:
        c += Rect2(x0=0, y0=0, x1=0.6, y1=0.6, label=r'{\texttt{%s}}' % '',
             linecolor='white')
    else:
        c += Rect2(x0=0, y0=0, x1=0.6, y1=0.6, label=r'{\texttt{%s}}' % x)

p += c

s = Rect2(x0=0, y0=-2, x1=0.6, y1=-2+0.6, label=r'{\texttt{%s}}' % '8')
p += s
p += Line(points=[s.top(), c[0].bottom()], endstyle='>')
print(p)


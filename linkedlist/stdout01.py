from latextool_basic import *
p = Plot()

c = RectContainer(x=0, y=0)
for i,x in enumerate('2645'):
    c += Rect2(x0=0, y0=0, x1=0.7, y1=0.7, label=r'{\texttt{%s}}' % x)
              
p += c

x,y = c[0].bottomleft(); x -= 2
q = Rect2(x0=x, y0=y, x1=x+0.7, y1=0.7, label=r'{\texttt{%s}}' % '')
p += q

x,y = q.left(); x -= 0.3
p += Rect2(x0=x, y0=y, x1=x, y1=y, label=r'{\texttt{%s}}' % 'p',
           linecolor='white')

p += Line(points=[q.center(), c[0].left()], endstyle='>')
print(p)

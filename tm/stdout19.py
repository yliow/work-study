from latextool_basic import *
p = Plot()

h = RectContainer(x=0, y=0, align='bottom', direction='left-to-right')
for i in [r'\DOLLAR', 'a','b',r'a$^*$','a','a','b','a', '$\sqcup$',
r'!','b','$\sqcup$','b','a','$\sqcup^*$','b','!'
]:
    h += Rect2(0,0,0.7,0.7, label= r'\texttt{%s}' % i,
               linewidth=0.01)
    p += h
p += Line(x0=h[-1].x1, y0=h[-1].y1, x1=h[-1].x1+0.5, y1=h[-1].y1,
     linewidth=0.01)
p += Line(x0=h[-1].x1, y0=h[-1].y0, x1=h[-1].x1+0.5, y1=h[-1].y0,
     linewidth=0.01)

x,y = h[1].bottom()
p += Line(points=[(x,y-0.5), (x,y)], endstyle='>')

print(p)

from latextool_basic import *
p = Plot()

h = RectContainer(x=0, y=0, align='bottom', direction='left-to-right')
for i in [r'$\BOT$', 'a','b','a','a','$\sqcup$','$\sqcup$','a', '$\sqcup$','$\sqcup$',]:
    h += Rect2(0,0,1,1, label= r'\texttt{%s}' % i,
               linewidth=0.01)
    p += h
p += Line(x0=h[-1].x1, y0=h[-1].y1, x1=h[-1].x1+0.5, y1=h[-1].y1,
     linewidth=0.01)
p += Line(x0=h[-1].x1, y0=h[-1].y0, x1=h[-1].x1+0.5, y1=h[-1].y0,
     linewidth=0.01)
print(p)

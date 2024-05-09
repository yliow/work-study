from latextool_basic import *
p = Plot()
c = RectContainer(x=0, y=0)
for i,x in enumerate('2645'):
    c += Rect2(x0=0, y0=0, x1=0.7, y1=0.7, label=r'{\texttt{%s}}' % x)
              
p += c

print(p)

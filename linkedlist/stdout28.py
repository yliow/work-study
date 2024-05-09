from latextool_basic import *
p = Plot()
c = RectContainer(x=1, y=1, align='bottom', direction='left-to-right')
for i, x in enumerate([3,5,6,7]):
    c += Rect2(x0=0, y0=0, x1=1, y1=0.7,
         label=r'{\texttt{%s}}' % x)

p += c

# boundary of container
p += Rect2(x0=c.x0, y0=c.y0, x1=c.x1, y1=c.y1, linewidth=0.1)

#p += Grid()
print(p)

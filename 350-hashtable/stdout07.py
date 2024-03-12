from latextool_basic import *
p = Plot()

C = RectContainer(x=1, y=1, direction='top-to-bottom', align='left')

for a,b,c,d in [(0, 'true' , ''     , ''),
                (1, 'true' , ''     , ''),
                (2, 'true' , ''     , ''),
                (3, 'true' , ''     , ''),
                (4, 'false', 'Tom'  , 5.5),
                (5, 'false', 'Abe'  , 6.5), 
                (6, 'false', 'Annie', 5.9),
                (7, 'true' , ''     , ''),
                (8, 'true' , ''     , ''),
                (9, 'true' , ''     , ''),
                ]:
    h = 0.6
    c0 = RectContainer(x=1, y=1)
    c0 += Rect2(x0=0, y0=0, x1=0.8, y1=h, 
                linewidth=0.02,label=r'{\texttt{%s}}' % a)
    c0 += Rect2(x0=0, y0=0, x1=3.5, y1=h, linecolor='black',
                linewidth=0.02,label=r'{\texttt{%s}}' % b)
    c0 += Rect2(x0=0, y0=0, x1=3, y1=h, 
                linewidth=0.02,label=r'{\texttt{%s}}' % c)
    c0 += Rect2(x0=0, y0=0, x1=1.5, y1=h, 
                linewidth=0.02,label=r'{\texttt{%s}}' % d)
    c0.layout()
    C += c0; c0.x = c0.x0; c0.y = c0.y0; c0.layout()

C.layout()
p += C

x0,y0 = C[5][0].left(); y0 -= 0.1
x1,y1 = C[6][0].left(); y1 += 0.1
p += Line(points=[(x0,y0), (x0-0.5,y0), (x0-0.5,y1), (x1,y1)], endstyle='>')

print(p)

from latextool_basic import *
p = Plot()

C = RectContainer(x=1, y=1, direction='top-to-bottom', align='left')

for a,b,c,d in [(0, 'Available' , ''     , ''),
                (1, 'Available' , ''     , ''),
                (2, 'Available' , ''     , ''),
                (3, 'Available' , ''     , ''),
                (4, 'Not-Available', 'Tom'  , 5.5),
                (5, 'Not-Available', 'Abe'  , 6.5), 
                (6, 'Not-Available', 'Annie', 5.9),
                (7, 'Deleted'      , 'Tammy', 6.2),
                (8, 'Not-Available', 'Andrew', 5.7),
                (9, 'Not-Available', 'Tania' , 6.7),
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

x0,y0 = C[6][0].left(); y0 -= 0.1
x1,y1 = C[8][0].left(); y1 += 0.1
p += Line(points=[(x0,y0), (x0-0.5,y0), (x0-0.5,y1), (x1,y1)], endstyle='>')


x0,y0 = C[4][0].left(); y0 -= 0.1
x1,y1 = C[7][0].left(); y1 += 0.1
p += Line(points=[(x0,y0), (x0-1.5,y0), (x0-1.5,y1), (x1,y1)],
          linecolor='blue', endstyle='>')

x0,y0 = C[7][0].left(); y0 -= 0.1
x1,y1 = C[9][0].left(); y1 += 0.1
p += Line(points=[(x0,y0), (x0-1.5,y0), (x0-1.5,y1), (x1,y1)],
          linecolor='blue', endstyle='>')

x0,y0 = C[7][3].right()
p += Line(points=[(x0+1,y0), (x0,y0)],
          linecolor='red', endstyle='>', linewidth=0.2)
print(p)

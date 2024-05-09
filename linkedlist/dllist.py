
from latextool_basic import *

SIZE = 0.5
LENGTH = 1.5
LINEWIDTH=0.02

def dlnode(x, y, s):
    c = RectContainer(x=x, y=y)
    c += Rect2(x0=0, y0=0, x1=SIZE, y1=SIZE, label=r'{\texttt{%s}}' % '', linewidth=LINEWIDTH)
    c += Rect2(x0=0, y0=0, x1=SIZE, y1=SIZE, label=r'{\texttt{%s}}' % s, linewidth=LINEWIDTH)
    c += Rect2(x0=0, y0=0, x1=SIZE, y1=SIZE, label=r'{\texttt{%s}}' % '', linewidth=LINEWIDTH)
    return c

def cross(r):
    return Line(points=[r.topleft(), r.bottomright()], linewidth=LINEWIDTH), Line(points=[r.topright(), r.bottomleft()], linewidth=LINEWIDTH)

def next(n0, n1):
    return Line(points=[n0[2].center(), n1[0].left()], endstyle='>', linewidth=LINEWIDTH)

def prev(n1, n0):
    x0,y0 = n1[0].center()
    y = y0 - 0.75
    x1,y1 = n0[2].bottom()
    return Line(points=[(x0,y0), (x0,y), (x1,y), (x1,y1)], endstyle='>', linewidth=LINEWIDTH)

def dllist(p, x=0, y=0, xs=[], start=0, end=-1, pheadstr='phead', ptailstr='ptail'):
    r = []
    for key in xs:
        n = dlnode(x, y, key)
        r.append(n)
        p += n
        x += 2
    for i,x in enumerate(xs):
        if i < len(xs) - 1:
            p += next(r[i], r[i+1])
        if i > 0:
            p += prev(r[i], r[i-1])
    l0, l1 = cross(r[0][0]); p += l0; p += l1
    l0, l1 = cross(r[-1][2]); p += l0; p += l1

    # phead's square
    x,y = r[start][1].bottomleft(); y -= LENGTH / 1.5
    q = Rect2(x0=x, y0=y, x1=x+SIZE, y1=y+SIZE, label=r'{\texttt{%s}}' % '', linewidth=LINEWIDTH)
    p += q
    # phead's label
    x,y = q.center(); y -= 0.5
    p += Rect2(x0=x, y0=y, x1=x, y1=y, label=r'{\texttt{%s}}' % pheadstr, linecolor='white', linewidth=LINEWIDTH)
    # phead to head
    p += Line(points=[q.center(), r[start].bottom()], endstyle='>', linewidth=LINEWIDTH)

    # ptail's square
    x,y = r[end][1].bottomleft(); y -= LENGTH
    q = Rect2(x0=x, y0=y, x1=x+SIZE, y1=y+SIZE, label=r'{\texttt{%s}}' % '', linewidth=LINEWIDTH)
    p += q
    # ptail's label
    x,y = q.center(); y -= 0.5
    p += Rect2(x0=x, y0=y, x1=x, y1=y, label=r'{\texttt{%s}}' % ptailstr, linecolor='white', linewidth=LINEWIDTH)
    # phead to head
    p += Line(points=[q.center(), r[end].bottom()], endstyle='>', linewidth=LINEWIDTH)

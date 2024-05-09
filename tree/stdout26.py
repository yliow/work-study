from latextool_basic import *

SIZE = 0.5
LENGTH = 1.5

def dlnode(x, y, s):
    c = RectContainer(x=x, y=y)
    c += Rect2(x0=0, y0=0, x1=SIZE, y1=SIZE, label=r'{\texttt{%s}}' % '')
    c += Rect2(x0=0, y0=0, x1=SIZE, y1=SIZE, label=r'{\texttt{%s}}' % s)
    c += Rect2(x0=0, y0=0, x1=SIZE, y1=SIZE, label=r'{\texttt{%s}}' % '')
    return c

def cross(r):
    return Line(points=[r.topleft(), r.bottomright()]), Line(points=[r.topright(), r.bottomleft()])

def next(n0, n1):
    return Line(points=[n0[2].center(), n1[0].left()], endstyle='>')

def prev(n1, n0):
    x0,y0 = n1[0].center()
    y = y0 - 0.5
    x1,y1 = n0[2].bottom()
    return Line(points=[(x0,y0), (x0,y), (x1,y), (x1,y1)], endstyle='>')

def dllist(p, x=0, y=0, k='', xs=[]):
    r = []
    oldx = x
    oldy = y
    if xs != []:
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
        x1,y1 = r[-1].topright()
        p += Rect(x0=oldx-0.25, y0=oldy-0.5, x1=x1+0.25, y1=y1+0.25)
    else:
        p += Rect(x0=oldx-0.25, y0=oldy-0.5, x1=oldx-0.25+0.25, y1=oldy+0.75)
    s = Rect(x0=oldx-0.25-0.5, y0=oldy-0.5, x1=oldx-0.25, y1=oldy+0.75,
        label=r'\texttt{%s}' % k)
    p += s
    r.append(s) 
    return r

p = Plot()
a = dllist(p, x=3, y=0, k='a', xs=['', '', ''])
b = dllist(p, x=0, y=-2, k='b', xs=['', ''])
c = dllist(p, x=5, y=-2, k='c', xs=[''])
d = dllist(p, x=8, y=-2, k='d', xs=['','',''])
e = dllist(p, x=0, y=-4, k='e', xs=['',''])
f = dllist(p, x=5, y=-4, k='f', xs=[])
g = dllist(p, x=6.25, y=-4, k='g', xs=[])
h = dllist(p, x=8, y=-4, k='h', xs=[''])
i = dllist(p, x=11.25, y=-4, k='i', xs=[])
j = dllist(p, x=13.25, y=-4, k='j', xs=[])
k = dllist(p, x=1.25, y=-6, k='k', xs=[])
l = dllist(p, x=3.25, y=-6, k='l', xs=[])
m = dllist(p, x=9.25, y=-6, k='m', xs=[])

def arr(p0, p1):
    x0, y0 = p0
    x1, y1 = p1
    return Line(points=[(x0,y0), (x0,y0-1), (x1,y0-1), (x1,y1)], endstyle='>')
    
p += arr(a[0].center(), b[-1].top())
p += arr(a[1].center(), c[-1].top())
p += arr(a[2].center(), d[-1].top())

p += arr(b[0].center(), e[-1].top())
p += arr(b[1].center(), f[-1].top())

p += arr(c[0].center(), g[-1].top())

p += arr(e[0].center(), k[-1].top())
p += arr(e[1].center(), l[-1].top())

p += arr(d[0].center(), h[-1].top())
p += arr(d[1].center(), i[-1].top())
p += arr(d[2].center(), j[-1].top())

p += arr(e[1].center(), l[-1].top())

p += arr(h[0].center(), m[-1].top())

print(p)

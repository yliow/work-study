from latextool_basic import *
p = Plot()

def cross(p, r):
    p += Line(points=[r.topleft(), r.bottomright()], linewidth=0.01)
    p += Line(points=[r.topright(), r.bottomleft()], linewidth=0.01)
    
c = RectContainer(x=0, y=0)
for x in ['' for _ in range(26)]:
    c += Rect2(x0=0, y0=0, x1=0.25, y1=0.25,
         label='', linewidth=0.01)

p += c
x0,y0 = c.bottomleft(); x0 -= 0.25; y0 -=0.25
x1,y1 = c.topright(); x1 += 0.25; y1 += 0.25
r0 = Rect2(x0=x0, y0=y0, x1=x1, y1=y1)
p += r0

for i in range(26):
    if i != 7:
        cross(p, c[i])
        
w = y1 - y0
r1 = Rect2(x0=x0 - w, y0=y0, x1=x0, y1=y1, label=r"\texttt{' '}")
p += r1


d = RectContainer(x=0, y=-2)
for x in ['' for _ in range(26)]:
    d += Rect2(x0=0, y0=0, x1=0.25, y1=0.25,
         label='', linewidth=0.01)

p += d
x0,y0 = d.bottomleft(); x0 -= 0.25; y0 -=0.25
x1,y1 = d.topright(); x1 += 0.25; y1 += 0.25
r0 = Rect2(x0=x0, y0=y0, x1=x1, y1=y1)
p += r0

for i in range(26):
    cross(p, d[i])

w = y1 - y0
r2 = Rect2(x0=x0 - w, y0=y0, x1=x0, y1=y1, label=r"\texttt{'*'}")
p += r2

x0,y0 = c[7].center()
x1,y1 = r2.top()
p += Line(points=[(x0,y0), (x0,y1)], endstyle='>')

print(p)

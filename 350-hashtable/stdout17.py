from latextool_basic import *

p = Plot()

v = RectContainer(x=2, y=0, align='left', direction='top-to-bottom')
for i in range(10):
    r = Rect2(0, 0, 0.5, 0.5)
    v += r

v.layout()

def node(x, y, key, value, null=True):
    c0 = RectContainer(x=x, y=y)
    c0 += Rect2(0, 0, 2, 0.5, label= r'\texttt{%s}' % key)
    c0 += Rect2(0, 0, 1.5, 0.5, label= r'\texttt{%s}' % value)
    c0 += Rect2(0, 0, 0.5, 0.5)
    return c0

for i in range(10):
    if i == 4:
        center = v[i].center()
        (x0, y0) = center
        (x1, y1) = (center[0] + 1, center[1] + 0.025)
        n = node(x1, y1, "Tom", 5.5)
        p += n
        x1, y1 = n.left()
        p += Line(x0=x0, y0=y0, x1=x1, y1=y1, linewidth=0.05, startstyle='dot', endstyle='>')
        x0, y0 = n[2].topleft()
        x1, y1 = n[2].bottomright()
        p += Line(x0, y0, x1, y1)
        x0, y0 = n[2].topright()
        x1, y1 = n[2].bottomleft()
        p += Line(x0, y0, x1, y1)
    elif i == 5:
        center = v[i].center()
        (x0, y0) = center
        (x1, y1) = (center[0] + 1, center[1] - 0.5)
        n = node(x1, y1, "Abe", 6.5)
        p += n

        (x0, y0) = center
        x1, y1 = n.left()
        p += Line(x0=x0, y0=y0, x1=x1, y1=y1, linewidth=0.05, startstyle='dot', endstyle='>')

        # node for annie
        x1, y1 = n[2].bottomleft()        
        n1 = node(x1 + 1.5, y1, "Annie", 5.9)
        p += n1
        # null pointer for n1
        x0, y0 = n1[2].topleft()
        x1, y1 = n1[2].bottomright()
        p += Line(x0, y0, x1, y1, linewidth=0.05)
        x0, y0 = n1[2].topright()
        x1, y1 = n1[2].bottomleft()
        p += Line(x0, y0, x1, y1, linewidth=0.05)
        # next pointer arrow
        x0, y0 = n[2].center()
        x1, y1 = n1[0].left()
        p += Line(x0, y0, x1, y1, linewidth=0.05, startstyle='dot', endstyle='>')
    else:
        topleft = v[i].topleft()
        bottomright = v[i].bottomright()
        (x0, y0) = topleft
        (x1, y1) = bottomright
        p += Line(x0=x0, y0=y0, x1=x1, y1=y1, linewidth=0.05)
        topright = v[i].topright()
        bottomleft = v[i].bottomleft()
        (x0, y0) = topright
        (x1, y1) = bottomleft
        p += Line(x0=x0, y0=y0, x1=x1, y1=y1, linewidth=0.05)

p += v
print(p)

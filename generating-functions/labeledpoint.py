from math import sin, cos, pi
from latexcircuit import *  

POLY_LINEWIDTH = 0.08
AXES_LINEWIDTH = 0.01

def IFELSE(b, x, y):
    if b: return x
    else: return y

            
def axes(p,x0=0,y0=0,x1=3,y1=3):
    p += Line(points=[(x0,y0), (x1,y0)], endstyle='>', linewidth=AXES_LINEWIDTH)
    p += Line(points=[(x0,y0), (x0,y1)], endstyle='>', linewidth=AXES_LINEWIDTH)

    
def labeledpoint(x=0, y=0, r='0.2cm',
                 label='', anchor='east', name=None, filled=True,
                 background='black',
                 drawpoints=True):
    if name==None: name=label
    s = ""
    if filled:
        s += r"\node[draw,shape=circle,minimum size=%s,fill=%s,inner sep=0](%s) at (%s,%s){};" % (r,background,name,x,y)
    else:
        s += r"\node[draw,shape=circle,minimum size=%s,fill=%s,inner sep=0](%s) at (%s,%s){};" % (r, 'white', name,x,y)    
    X = POINT(x=x, y=y, r=0, label=label, anchor=anchor)
    s += str(X)
    return s


def polygon(points=None, names=None,
            background=None, # if background if None, no fill
            linewidth=None,
            linecolor=None,
            fill=True,
            drawboundary=True,
            closed=True,
    ):
    """ names does not work. use points """
    n = None
    if fill or background:
        fill = True
        if not background: background = 'gray'
    else:
        fill = False
        background = None    
    if points:
        if closed:
            if points[0] != points[-1]:
                points.append(points[0])
        points_str = " -- ".join(["(%s,%s)" % (x,y) for (x,y) in points])
        n = len(points)
    if names:
        points_str = " -- ".join(["(%s)" % name for name in names])
        n = len(names)
    interior = IFELSE(fill, "fill=%s, fill opacity=0.2" % background, '')

    boundary = ''
    if drawboundary or linewidth or linecolor:
        drawboundary = True
        if not linecolor: linecolor='black'
        if not linewidth: linewidth=POLY_LINEWIDTH
        boundary = 'draw=%s, line width=%scm,' % (linecolor, linewidth)

    s = ""
        
    #if fill:
    #    s += r"\fill [%s] %s;" % (interior, points_str)
    #
    #if drawboundary:
    #    s += r"\path [%s, %s] %s;" % (interior, boundary, points_str)

    s += r"\path [%s, %s] %s;" % (interior, boundary, points_str)

    #for i in range(len(points)):
    #    x,y = points[i]
    #    x1,y1 = points[(i + 1) % n]
    #    s += str(Line(points=[(x,y),(x1,y1)]))

    return s


def poly1(p,
          fill=True,
          drawpoints=True,
          drawlabels=True):
    V = [(1,1), (0.8,2), (1.5,3), (3, 2.5), (2, 4), (4,3.5), (4.5, 2.5), (4.3, 1), (3,1.5), (2,0.5)]
    V = V[::-1]
    n = len(V)

    p += polygon(points=V, fill=fill)

    anchors = ['east', 'east', 'south', 'west', 'south', 'west', 'west', 'north', 'south', 'north'][::-1]

    if drawpoints:
        for i,anchor in enumerate(anchors):
            x,y = V[i]
            if drawlabels:
                label = '$v_%s$' % i
            else:
                label = ''
            p += labeledpoint(x, y, label=label, name='%s' % i,
                              anchor=anchor, drawpoints=drawpoints)
    return V

def chvatalcomb(p, k=4, fill=True, drawpoints=False):
    '''
    k = number of spikes


         *     *
        / \   / \
       /   ---   ---
      +------
    '''
    #V = [(0,0), (2,7), (3,1), (4, 1),
    #            (5,7), (6,1), (7, 1),
    #            (8,7), (9,1), (10,1),
    #            (11,7), (13,0)]

    V = [(0,0)]
    i = 0
    x = 1
    h = 9
    while i < k - 1:
        V += [(x,h), (x+1,1), (x+3,1)]
        i += 1; x += 4
    V += [(x,h), (x+1,0)]
    # scale down
    for i in range(len(V)):
        V[i] = (V[i][0]*0.4, V[i][1] * 0.4)
    
    V = V[::-1]
    n = len(V)

    p += polygon(points=V, fill=fill)

    anchors = ['east', 'east', 'south', 'west', 'south', 'west', 'west', 'north', 'south', 'north'][::-1]

    if drawpoints:
        for i,anchor in enumerate(anchors):
            x,y = V[i]
            p += labeledpoint(x, y, label='', name='',
                              anchor=anchor, drawpoints=drawpoints)
    return V


def regularpoly(n):
    r = 1.5
    V = []
    if n % 2 == 1:
        t = pi/2
    else:
        t = 0
    for i in range(n):
        x = r * cos(t)
        y = r * sin(t)
        V.append((x,y))
        t += 2 * math.pi / n
    return V

def stdpoly(p,
            n=3,
            typ='a',
            fill=True,
            drawpoints=True,
            drawlabels=True):
    if typ == 'a':
        V = regularpoly(n)
    p += polygon(points=V, fill=fill)

    return V

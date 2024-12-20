from latextool_basic import *
from latexcircuit import *

def heaparray(x, y, width=0.4, height=0.4, xs='1325'):
    c = RectContainer(x=x, y=y)
    for x in xs:
        c += Rect2(x0=0, y0=0, x1=width, y1=height,
                   linewidth=0.02,
                   label=r'{\footnotesize \texttt{%s}}' % x)
    return c

def intdynarr(p, x=1, y=1,
              label='a', height=0.4, width=0.4, vsep=0.15,
              members=[('x',''), ('size',''), ('capacity','')],
              LENGTH=1.6,
              do_not_draw=False):
    
    # NOTE:  
    num_boundary = [] # b1, b2, ...
    boundaries = []

    # Note x,y is coord of 1st var box
    rect = {}
    for name,value in members:
        r = Rect(x0=x, y0=y, x1=x + width, y1=y + height, label=r'{\footnotesize \texttt{%s}}' % value) # box for first var
        rect[name] = r
        if not do_not_draw:
            p += r
        x0,y0 = r.left()
        if not do_not_draw:
            p += str(POINT(x=x0, y=y0, r=0, label=r'{\footnotesize \texttt{%s}}' % name, anchor='east'))
        y -= height + vsep
        
    #r1 = Rect(x0=x, y0=y, x1=x + width, y1=y + height) # box for first var
    #y -= height + vsep
    #r2 = Rect(x0=x, y0=y, x1=x + width, y1=y + height) # box for second var
    #y -= height + vsep
    #r3 = Rect(x0=x, y0=y, x1=x + width, y1=y + height) # box for third var
    #y -= vsep

    # Put a dummy box at the top left corner
    # LENGTH = 2 -- distance from left of varbox to object box
    x1,y1 = rect[members[0][0]].topright(); x1 += vsep; y1 += vsep
    x0,y0 = rect[members[-1][0]].bottomleft(); x0 -= vsep; y0 -= vsep; x0 -= LENGTH
    r0 = Rect(x0=x0, y0=y0, x1=x1, y1=y1, background='')
    if not do_not_draw: p += r0
    rect[label] = r0

    # bounding box name
    x,y = r0.left()
    if not do_not_draw:
        p += str(POINT(x=x, y=y, r=0, label=r'\texttt{%s}' % label, anchor='east'))

    return rect

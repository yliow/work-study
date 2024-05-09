from latextool_basic import *

widths= [0, 0.61]
height = 0.4
THICKLINEWIDTH = 0.08

def IFELSE(b, x, y):
    if b: return x
    else: return y
    
def f(M, star=False, n=4):
    if len(M) > n: n = len(M)
    M = M + ['' for _ in range(n - len(M))]
    if star:
        M = g(M)
    return [r'{{\scriptsize\texttt{%s}}}' % _ for _ in M]
def g(M):
    return [IFELSE(_=='', '', r'{%s$_*$}' % _) for _ in M]

def bpt_node_(x, y, M, linecolor='black'):
    return bpt_node(x=x, y=y, M=M, widths=widths, height=height,
                    linewidth=0.04, linecolor=linecolor)

def get_bpt_nodes(names, M, d):
    N = {}
    for i,(name,m) in enumerate(zip(names, M)):
        x,y = d[name]
        if all([_ == '' for _ in m]):
            N[name] = bpt_node_(x=x, y=y, M=m, linecolor='white')
        else:
            N[name] = bpt_node_(x=x, y=y, M=m)
    return N

def dllist(p, names, N):
    for n0,n1 in zip(names[:-1], names[1:]):
        x0,y0 = N[n0].bottomright(); p0 = (x0-0.25, y0)
        x1,y1 = N[n1].bottomleft(); p1 = (x1+0.25,y1)
        p += bend(p0, p1, dy=-0.5, linewidth=0.02)

def highlight(rect):
    x0,y0 = rect.bottomleft()
    x1,y1 = rect.topright()
    return Rect2(x0=x0, y0=y0, x1=x1, y1=y1,
           linecolor='red', linewidth=THICKLINEWIDTH)
